from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
from website.decorators.auth import is_authenticated, has_permission
from website.models.game_dao import Game, GameDAO
from website.models.complaint_dao import Complaint, ComplaintDAO
from website.models.full_complaint_dao import FullComplaintDAO

complaints = Blueprint('complaints', __name__)

@is_authenticated
@complaints.route('/games/<int:id>/add-complaint', methods=['GET', 'POST'])
def add_complaint(id):
    if request.method == 'POST':
        game_id = id
        text = request.form.get('text')
        type = request.form.get('type')

        cursor = mysql.connection.cursor()
        game = GameDAO().find_by_id(cursor, id)

        if game:
            complaint = Complaint(user_id=session['user_id'], game_id=game_id, complaint_type=type, complaint_text=text, complaint_id=None, solved=None, created_at=None)
            ComplaintDAO().add(cursor, complaint)
            mysql.connection.commit()
            
            flash('Problema relatado, aguarde a revisão do pedido.', category='success')
            return redirect(url_for('games.get_games'))
        else:
            flash('Id fornecido não existe.', category='error')
            return redirect(url_for('complaints.add_complaint'))

    return render_template('add-complaint.html', session=session, game_id=id)

@complaints.route('/complaints', methods=['GET', 'POST'], strict_slashes=False)
@is_authenticated
def get_complaints():
    cursor = mysql.connection.cursor()
    full_complaints = FullComplaintDAO().filter_by_user_id(cursor, session['user_id'])
    
    return render_template('complaints.html', session=session, complaints=full_complaints)

@complaints.route('/delete-complaint', methods=['POST'])
def delete_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    cursor = mysql.connection.cursor()
    complaint = ComplaintDAO().find_by_id(cursor, complaintId)

    if complaint:
        if complaint.user_id == session['user_id']:
            ComplaintDAO().delete(cursor, complaint.complaint_id)
            mysql.connection.commit()
    
    return jsonify({})

@is_authenticated
@complaints.route('/complaints/<int:id>/update', methods=['GET', 'POST'])
def update_complaint(id):
    cursor = mysql.connection.cursor()
    complaint = ComplaintDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        if complaint.user_id == session['user_id']:
            game_id = request.form.get('game_id')
            text = request.form.get('text')
            type = request.form.get('type')

            updated_game_id = complaint.game_id
            updated_text = complaint.complaint_text
            updated_type = complaint.complaint_type

            if game_id:
                game = GameDAO().find_by_id(cursor, game_id)

                if not game:
                    flash('Id de jogo não existe dado não existe', category='error')
                    return redirect(url_for('complaints.update_complaint', id=complaint.complaint_id))
                else:
                    updated_game_id = game_id
            
            if text:
                updated_text = text
            
            if type:
                updated_type = type

            updated_complaint = Complaint(complaint_id=complaint.complaint_id, game_id=updated_game_id, complaint_text=updated_text, complaint_type=updated_type, solved=complaint.solved, user_id=None, created_at=None)
            ComplaintDAO().update(cursor, updated_complaint)
            mysql.connection.commit()
            flash('Denúncia atualizada', category='success')
            return redirect(url_for('complaints.get_complaints'))
        else:
            flash('Denúncia pedida não foi feita pelo usuário conectado', category='error')
            return redirect(url_for('complaints.get_complaints'))

    return render_template("update-complaint.html", session=session)

@complaints.route('/complaints/manage')
@is_authenticated
@has_permission('admin')
def manage_complaints():
    cursor = mysql.connection.cursor()
    full_complaints = FullComplaintDAO().get_all(cursor)

    return render_template("manage-complaints.html", session=session, complaints=full_complaints)

@complaints.route('/check-complaint', methods=['POST'])
@is_authenticated
def check_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    cursor = mysql.connection.cursor()
    complaint = ComplaintDAO().find_by_id(cursor, complaintId)

    if complaint:
        if session['user_permission'] == "admin":
            updated_complaint = Complaint(complaint_id=complaint.complaint_id, user_id=complaint.user_id, game_id=complaint.game_id, complaint_type=complaint.complaint_type, complaint_text=complaint.complaint_text, solved=1, created_at=complaint.created_at)
            ComplaintDAO().update(cursor, updated_complaint)
            mysql.connection.commit()
    
    return jsonify({})

@complaints.route('/uncheck-complaint', methods=['POST'])
@is_authenticated
def uncheck_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    cursor = mysql.connection.cursor()
    complaint = ComplaintDAO().find_by_id(cursor, complaintId)

    if complaint:
        if session['user_permission'] == "admin":
            updated_complaint = Complaint(complaint_id=complaint.complaint_id, user_id=complaint.user_id, game_id=complaint.game_id, complaint_type=complaint.complaint_type, complaint_text=complaint.complaint_text, solved=0, created_at=complaint.created_at)
            ComplaintDAO().update(cursor, updated_complaint)
            mysql.connection.commit()
    
    return jsonify({})