from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from flask_login import login_required, current_user
from .models import Game, Image
from . import db
import json
from werkzeug.utils import secure_filename

posts = Blueprint('posts', __name__)

@login_required
@posts.route('/add-game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer = request.form.get('developer')
        publisher = request.form.get('publisher')

        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img = Image(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()

        new_game = Game(title=title, release_date=release_date, description=description, developer=developer, publisher=publisher, cover_picture=img.id)
        db.session.add(new_game)
        db.session.commit()
        flash('Jogo adicionado!', category='success')
        return redirect(url_for('posts.games'))

    return render_template('add-game.html', user=current_user)

@posts.route('/games')
def games():
    games = Game.query.order_by(Game.release_date)
    return render_template("games.html", user=current_user, games=games)

@posts.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        pic = request.files['pic']

        if not pic:
            return 'No pic uploaded.'

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img = Image(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()
        flash('Imagem adicionada com sucesso', category='success')

    return render_template("upload.html", user=current_user)

@posts.route('/image')
def get_image_page():
    return render_template("image.html", user=current_user)

@posts.route('/image/<int:id>')
def get_image(id):
    img = Image.query.filter_by(id=id).first()
    if not img:
        return redirect(url_for('views.home'))

    return Response(img.img, mimetype=img.mimetype)