from website import app, mysql
from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from .models import Note, Game, User, Complaint
from . import db
import json
from website.decorators.auth import is_authenticated, has_permission
from website.models_p.user_dao import UserDAO
from website.models_p.complaint_dao import ComplaintDAO
from website.models_p.library_game_dao import LibraryGameDAO
from website.models_p.review_dao import ReviewDAO
from website.models_p.note_dao import NoteDAO

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    print(session)
    return render_template("home.html", notes=Note.query.all(), session=session)

@views.route('/notes', methods=['GET', 'POST'])
@is_authenticated
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    cursor = mysql.connection.cursor()
    notes = NoteDAO().filter_by_user_id(cursor, session['user_id'])

    return render_template("notes.html", session=session, notes=notes)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})

@views.route('/dashboard', methods=['POST', 'GET'])
@is_authenticated
def dashboard():
    cursor = mysql.connection.cursor()

    if session['user_permission'] == "admin":
        users = UserDAO().get_all(cursor)
        complaints = ComplaintDAO().get_all(cursor)

        admin_info_dict = {
            "users": len(users),
            "unsolved_complaints": len([c for c in complaints if not c.solved])
        }
    else:
        admin_info_dict = dict()

    user = UserDAO().find_by_id(cursor, session['user_id'])
    library_games = LibraryGameDAO().filter_by_user_id(cursor, session['user_id'])
    reviews = ReviewDAO().filter_by_user_id(cursor, session['user_id'])
    complaints = ComplaintDAO().filter_by_user_id(cursor, session['user_id'])
    complaints_solved = [c.solved for c in complaints]
    complaints_solved_dict = {
        "solved": sum(complaints_solved),
        "unsolved": len(complaints_solved) - sum(complaints_solved)
    }

    return render_template("dashboard.html", session=session, user=user, library_games=library_games, reviews=reviews, complaints_solved=complaints_solved_dict, admin_info=admin_info_dict)