from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify
from flask_login import login_required, current_user
from .models import Game, Image, LibraryGame, Screenshot, Review
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
        trailer_url = request.form.get('trailer_url')

        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img = Image(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()

        new_game = Game(title=title, release_date=release_date, description=description, developer=developer, publisher=publisher, trailer_url=trailer_url, cover_picture=img.id)
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

@posts.route('/games/<int:id>', methods=['GET', 'POST'])
def get_game(id):
    game = Game.query.get_or_404(id)

    if request.method == 'POST':
        text = request.form.get("text")
        score = request.form.get("score")
        review = Review(user_id=current_user.id, game_id=id, text=text, score=score)

        db.session.add(review)
        db.session.commit()
        flash('Análise publicada.', category='success')
    
    reviews = Review.query.filter_by(game_id=id).order_by(Review.date_created.desc())

    return render_template("game.html", user=current_user, game=game, reviews=reviews)

@posts.route('/add-to-library', methods=['POST'])
def add_to_library():
    data = json.loads(request.data)
    gameId = data['gameId']
    game = Game.query.get(gameId)

    relations = LibraryGame.query.filter_by(user_id=current_user.id)
    games_in_library = [r.game_id for r in relations]

    if gameId in games_in_library:
        flash("Jogo já está na sua biblioteca.", category="error")
    elif game:
        game_to_user = LibraryGame(user_id=current_user.id, game_id=gameId, spent_hours = 0, percentage_done = 0)
        db.session.add(game_to_user)
        db.session.commit()
        flash("Jogo adicionado com sucesso à sua biblioteca!", category="success")
    
    return jsonify({})

@login_required
@posts.route('/library')
def library():
    full_library_games = LibraryGame.query.join(Game, LibraryGame.game_id == Game.id).add_columns(Game.id, Game.title, Game.cover_picture, LibraryGame.spent_hours, LibraryGame.percentage_done, LibraryGame.last_logged, LibraryGame.user_id).filter(LibraryGame.game_id == Game.id, LibraryGame.user_id == current_user.id)

    return render_template("library.html", user=current_user, games=full_library_games)

@login_required
@posts.route('/library/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def get_game_in_library(id):
    library_game = LibraryGame.query.filter_by(user_id=current_user.id, game_id=id).first()
    game = Game.query.filter_by(id=id).first()

    if request.method == 'POST':
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        img = Image(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()

        screenshot = Screenshot(pic_id=img.id, user_id=current_user.id, game_id=id)
        db.session.add(screenshot)
        db.session.commit()

    screenshots = Screenshot.query.filter_by(user_id=current_user.id, game_id=id)

    return render_template("library_game.html", user=current_user, library_game=library_game, game=game, screenshots=screenshots)

@login_required
@posts.route('/remove-from-library', methods=['POST'])
def remove_from_library():
    data = json.loads(request.data)
    gameId = data['gameId']
    relation = LibraryGame.query.filter_by(user_id=current_user.id, game_id=gameId).first()

    if relation:
        db.session.delete(relation)
        db.session.commit()
        flash("Jogo removido da sua biblioteca com sucesso", category="success")
    
    return jsonify({})

@login_required
@posts.route('/library/<int:id>/delete')
def delete_from_library(id):
    game = LibraryGame.query.filter_by(game_id=id).first()

    db.session.delete(game)
    db.session.commit()
    flash('Jogo removido da biblioteca', category='success')

    return redirect(url_for('posts.library'))

@login_required
@posts.route('/library/<int:id>/update', methods=['GET', 'POST'])
def update_library(id):
    game = LibraryGame.query.filter_by(game_id=id, user_id=current_user.id).first()

    if request.method == 'POST':
        spent_hours = request.form.get('spent_hours')
        percentage_done = request.form.get('percentage_done')
        last_logged = request.form.get('last_logged')

        if spent_hours:
            print("odasdas")
            game.spent_hours = spent_hours
        if percentage_done:
            game.percentage_done = percentage_done
        
        db.session.commit()
        flash('Dados atualizados!', category='success')
        return redirect(url_for('posts.get_game_in_library', id=game.game_id))

    return render_template("update-library.html", user=current_user, game=game)

@posts.route('/delete-review', methods=['POST'])
def delete_review():
    data = json.loads(request.data)
    reviewId = data['reviewId']
    review = Review.query.get(reviewId)
    if review:
        if review.user_id == current_user.id:
            db.session.delete(review)
            db.session.commit()
    
    return jsonify({})