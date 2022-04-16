from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Image
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Conectou-se com sucesso!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Senha incorreta, tente novamente.', category='error')
        else:
            flash('E-mail não existe.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Desconectou-se.', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        pic = request.files['pic']

        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-mail já existe.', category='error')
        elif len(email) < 4:
            flash('E-mail precisa ter mais de 3 caracteres.', category='error')
        elif len(firstName) < 2:
            flash('Primeiro nome precisa ter mais de 1 caracter.', category='error')
        elif password1 != password2:
            flash('Senhas não batem.', category='error')
        elif len(password1) < 7:
            flash('Senha precisa ter pelo menos 7 caracteres.', category='error')
        else:
            if pic:
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype
                img = Image(img=pic.read(), mimetype=mimetype, name=filename)
                db.session.add(img)
                db.session.commit()
                profile_picture = img.id
            else:
                profile_picture = 1

            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='sha256'), profile_picture=profile_picture)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)

@auth.route('/update-profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        pic = request.files['pic']
        if pic:
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            img = Image(img=pic.read(), mimetype=mimetype, name=filename)
            db.session.add(img)
            db.session.commit()
            profilePicture = img.id
        if email:
            user = User.query.filter_by(email=email).first()
            if user.email != current_user.email:
                flash('E-mail já existe.', category='error')
        elif email and (len(email) < 4):
            flash('E-mail precisa ter mais de 3 caracteres.', category='error')
        elif firstName and (len(firstName) < 2):
            flash('Primeiro nome precisa ter mais de 1 caracter.', category='error')
        elif password1 and (password1 != password2):
            flash('Senhas não batem.', category='error')
        elif password1 and (len(password1) < 7):
            flash('Senha precisa ter pelo menos 7 caracteres.', category='error')
        else:
            current_user.email = email
            if firstName:
                current_user.first_name = firstName
            if password1:
                current_user.password = generate_password_hash(password1, method='sha256')
            if pic:
                current_user.profile_picture = profilePicture
            db.session.commit()
            flash('Perfil atualizado!', category='success')
            return redirect(url_for('views.dashboard'))

    return render_template("update-profile.html", user=current_user)

@auth.route('/delete-profile', methods=['GET', 'POST'])
@login_required
def delete_profile():
    user_to_delete = User.query.get_or_404(current_user.id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Perfil excluído com sucesso!", category="success")
        return redirect(url_for('views.home'))
    except:
        flash("Não foi possível excluir o perfil.", category="error")
        return redirect(url_for('views.home'))