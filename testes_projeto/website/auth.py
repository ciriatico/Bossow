from website import app, mysql
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Image
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from website.models_p.user_dao import User, UserDAO
from website.decorators.auth import is_authenticated, has_permission
from website.models_p.image_dao import Image, ImageDAO

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    [session.pop(key) for key in list(session.keys())]
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        cursor = mysql.connection.cursor()
        user = UserDAO().find_by_email(cursor, email)
        if user:
            if user.password == password:
                session['user_id'] = user.id
                session['user_email'] = user.email
                session['user_permission'] = user.role

                flash('Conectou-se com sucesso!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não existe.', category='error')

    return render_template("login.html", user=current_user, session=session)

@auth.route('/logout')
@is_authenticated
def logout():
    [session.pop(key) for key in list(session.keys())]
    flash('Desconectou-se.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
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
                img = Image(id=None, img=pic.read(), mimetype=mimetype, filename=filename, created_at=None)
                ImageDAO().add(cursor, img)
                mysql.connection.commit()

                profile_picture = cursor.lastrowid
            else:
                profile_picture = 1

            new_user = User(id=None, email=email, password=password1, full_name=fullName, role="user", created_at=None, profile_picture=profile_picture)
            UserDAO().add(cursor, new_user)
            mysql.connection.commit()
            
            session['user_id'] = cursor.lastrowid
            session['user_email'] = new_user.email
            session['user_permission'] = new_user.role

            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)

@auth.route('/update-profile', methods=['GET', 'POST'])
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
            img = Image(id=None, img=pic.read(), mimetype=mimetype, filename=filename, created_at=None)
            ImageDAO().add(cursor, img)
            mysql.connection.commit()

            profile_picture = cursor.lastrowid
        else:
            profile_picture = user_now.profile_picture

        if email:
            user = UserDAO().find_by_email(cursor, email)
            if user and (user.email != session['user_email']):
                flash('E-mail já existe.', category='error')
        elif email and (len(email) < 4):
            flash('E-mail precisa ter mais de 3 caracteres.', category='error')
        elif fullName and (len(fullName) < 2):
            flash('Primeiro nome precisa ter mais de 1 caracter.', category='error')
        elif password1 and (password1 != password2):
            flash('Senhas não batem.', category='error')
        elif password1 and (len(password1) < 7):
            flash('Senha precisa ter pelo menos 7 caracteres.', category='error')

        if not email:
            email = user_now.email

        if not password1:
            password1 = user_now.password

        if not fullName:
            fullName = user_now.full_name
        
        role = user_now.role
        created_at = user_now.created_at

        updated_user = User(id=user_now.id, email=email, password=password1, full_name=fullName, role=role, created_at=created_at, profile_picture=profile_picture)
        UserDAO().update(cursor, updated_user)
        mysql.connection.commit()

        flash('Perfil atualizado!', category='success')
        return redirect(url_for('views.dashboard'))

    return render_template("update-profile.html", user=current_user)

@auth.route('/delete-profile', methods=['GET', 'POST'])
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