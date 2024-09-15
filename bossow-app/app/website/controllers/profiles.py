from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.full_library_dao import FullLibrary, FullLibraryDAO
from website.models.image_dao import Image, ImageDAO
from website.models.review_dao import Review, ReviewDAO
from website.models.full_review_dao import FullReviewDAO
from website.models.library_dao import Library, LibraryDAO
from website.models.note_dao import NoteDAO
from website.models.user_dao import User, UserDAO
from website.models.complaint_dao import Complaint, ComplaintDAO
from website.models.full_complaint_dao import FullComplaintDAO

profiles = Blueprint('profiles', __name__)

@profiles.route('/login', methods=['GET', 'POST'])
def login():
    [session.pop(key) for key in list(session.keys())]
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor = mysql.connection.cursor()
        user = UserDAO().find_by_email(cursor, email)
        if user:
            if user.password == password:
                session['user_id'] = user.user_id
                session['user_email'] = user.user_email
                session['user_permission'] = user.role

                flash('Conectou-se com sucesso!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não existe.', category='error')

    return render_template("login.html", session=session)

@profiles.route('/logout')
@is_authenticated
def logout():
    [session.pop(key) for key in list(session.keys())]
    flash('Desconectou-se.', category='success')
    return redirect(url_for('profiles.login'))

@profiles.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        pic = request.files['pic']

        cursor = mysql.connection.cursor()
        user = UserDAO().find_by_email(cursor, email)
        if user:
            flash('E-mail já existe.', category='error')
        elif len(email) < 4:
            flash('E-mail precisa ter mais de 3 caracteres.', category='error')
        elif len(fullName) < 2:
            flash('Primeiro nome precisa ter mais de 1 caracter.', category='error')
        elif password1 != password2:
            flash('Senhas não batem.', category='error')
        elif len(password1) < 7:
            flash('Senha precisa ter pelo menos 7 caracteres.', category='error')
        else:
            if pic:
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype
                image = Image(pic_id=None, data=pic.read(), mime_type=mimetype, file_name=filename, created_at=None)
                ImageDAO().add(cursor, image)
                mysql.connection.commit()

                profile_picture = cursor.lastrowid
            else:
                profile_picture = 1

            new_user = User(user_id=None, user_email=email, password=password1, full_name=fullName, role="user", created_at=None, profile_picture=profile_picture)
            UserDAO().add(cursor, new_user)
            mysql.connection.commit()
            
            session['user_id'] = cursor.lastrowid
            session['user_email'] = new_user.user_email
            session['user_permission'] = new_user.role

            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", session=session)

@profiles.route('/update-profile', methods=['GET', 'POST'])
@is_authenticated
def update_profile():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        user_now = UserDAO().find_by_id(cursor, session['user_id'])

        email = request.form.get('email')
        fullName = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        pic = request.files['pic']
        if pic:
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            image = Image(pic_id=None, data=pic.read(), mime_type=mimetype, file_name=filename, created_at=None)
            ImageDAO().add(cursor, image)
            mysql.connection.commit()

            profile_picture = cursor.lastrowid
        else:
            profile_picture = user_now.profile_picture

        if email:
            user = UserDAO().find_by_email(cursor, email)
            if user and (user.user_email != session['user_email']):
                flash('E-mail já existe.', category='error')
                return redirect(url_for('views.dashboard'))
        elif email and (len(email) < 4):
            flash('E-mail precisa ter mais de 3 caracteres.', category='error')
            return redirect(url_for('views.dashboard'))
        elif fullName and (len(fullName) < 2):
            flash('Primeiro nome precisa ter mais de 1 caracter.', category='error')
            return redirect(url_for('views.dashboard'))
        elif password1 and (password1 != password2):
            flash('Senhas não batem.', category='error')
            return redirect(url_for('views.dashboard'))
        elif password1 and (len(password1) < 7):
            flash('Senha precisa ter pelo menos 7 caracteres.', category='error')
            return redirect(url_for('views.dashboard'))

        if not email:
            email = user_now.user_email
        if not password1:
            password1 = user_now.password
        if not fullName:
            fullName = user_now.full_name
        
        role = user_now.role
        created_at = user_now.created_at

        updated_user = User(user_id=user_now.user_id, user_email=email, password=password1, full_name=fullName, role=role, created_at=created_at, profile_picture=profile_picture)
        UserDAO().update(cursor, updated_user)
        mysql.connection.commit()

        flash('Perfil atualizado!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("update-profile.html", session=session)

@profiles.route('/delete-profile', methods=['GET', 'POST'])
@is_authenticated
def delete_profile():
    try:
        cursor = mysql.connection.cursor()
        UserDAO().delete(cursor, session['user_id'])
        mysql.connection.commit()
        [session.pop(key) for key in list(session.keys())]

        flash("Perfil excluído com sucesso!", category="success")
        return redirect(url_for('views.home'))
    except:
        flash("Não foi possível excluir o perfil.", category="error")
        return redirect(url_for('views.home'))

@profiles.route('/profile/manage')
@is_authenticated
@has_permission("admin")
def manage_profiles():
    cursor = mysql.connection.cursor()
    users = UserDAO().get_all(cursor)
    return render_template("profiles.html", session=session, users=users)

@profiles.route('/profile/<int:id>', methods=['GET', 'POST'])
@is_authenticated
def get_profile(id):
    cursor = mysql.connection.cursor()

    profile = UserDAO().find_by_id(cursor, id)
    notes = NoteDAO().filter_by_user_id(cursor, id)
    full_reviews = FullReviewDAO().find_by_user_id(cursor, id)
    full_library_games = FullLibraryDAO().find_by_user_id(cursor, id)
    full_complaints = FullComplaintDAO().filter_by_user_id(cursor, id)

    if request.method == 'POST':
        role = request.form.get('role')
        updated_profile = User(user_id=profile.user_id, user_email=profile.user_email, password=profile.password, full_name=profile.full_name, role=role, created_at=profile.created_at, profile_picture=profile.profile_picture)
        UserDAO().update(cursor, updated_profile)
        mysql.connection.commit()

        profile = updated_profile

    return render_template("profile.html", session=session, profile=profile, reviews=full_reviews, complaints=full_complaints, library_games=full_library_games)
