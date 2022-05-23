from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.note_dao import Note, NoteDAO

notes = Blueprint('notes', __name__)

@notes.route('/notes', methods=['GET', 'POST'])
@is_authenticated
def get_notes():
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        data = request.form.get('note')

        if len(data) < 1:
            flash('Lembrete muito curto!', category='error')
        else:
            new_note = Note(user_id=session['user_id'], note_text=data, note_id=None, created_at=None)
            NoteDAO().add(cursor, new_note)
            mysql.connection.commit()

            flash('Lembrete adicionado!', category='success')

    notes = NoteDAO().filter_by_user_id(cursor, session['user_id'])

    return render_template("notes.html", session=session, notes=notes)

@notes.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']

    cursor = mysql.connection.cursor()
    note = NoteDAO().find_by_id(cursor, noteId)

    if note:
        if note.user_id == session['user_id']:
            NoteDAO().delete(cursor, note.note_id)
            mysql.connection.commit()

            flash('Lembrete removido!', category='success')
    
    return jsonify({})