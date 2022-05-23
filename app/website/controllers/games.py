from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.image_dao import Image, ImageDAO
from website.models.game_dao import Game, GameDAO
from website.models.review_dao import Review, ReviewDAO
from website.models.full_review_dao import FullReviewDAO
from website.models.developer_dao import DeveloperDAO
from website.models.full_developer_dao import FullDeveloperDAO
from website.models.publisher_dao import PublisherDAO
from website.models.full_publisher_dao import FullPublisherDAO
from website.models.console_dao import ConsoleDAO
from website.models.available_dao import Available, AvailableDAO
from website.models.full_available_dao import FullAvailableDAO

games = Blueprint('games', __name__)

@games.route('/games', strict_slashes=False)
def get_games():
    cursor = mysql.connection.cursor()
    games = GameDAO().get_all_sorted(cursor, 'release_date')
    return render_template("games.html", games=games, session=session)

@is_authenticated
@games.route('/add-game', methods=['GET', 'POST'])
def add_game():
    cursor = mysql.connection.cursor()
    developers = DeveloperDAO().get_all(cursor)
    publishers = PublisherDAO().get_all(cursor)
    consoles = ConsoleDAO().get_all(cursor)

    if request.method == 'POST':
        title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer_id = request.form.get('developer')
        publisher_id = request.form.get('publisher')
        trailer_url = request.form.get('trailer_url')
        console_ids = request.form.getlist('console')

        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype

        image = Image(pic_id=None, data=pic.read(), mime_type=mimetype, file_name=filename, created_at=None)
        ImageDAO().add(cursor, image)
        mysql.connection.commit()
        cover_picture = cursor.lastrowid

        add_game = Game(game_id=None, game_title=title, release_date=release_date, description=description, developer_id=developer_id, publisher_id=publisher_id, trailer_url=trailer_url, cover_picture=cover_picture)
        GameDAO().add(cursor, add_game)
        mysql.connection.commit()

        game_id = cursor.lastrowid

        for console_id in console_ids:
            new_available = Available(game_id=game_id, console_id=console_id)
            AvailableDAO().add(cursor, new_available)
            mysql.connection.commit()
        
        flash('Jogo adicionado!', category='success')
        return redirect(url_for('games.get_game', id=game_id))

    return render_template('add-game.html', session=session, developers=developers, publishers=publishers, consoles=consoles)

@games.route('/games/<int:id>', methods=['GET', 'POST'])
def get_game(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)
    full_developer = FullDeveloperDAO().find_by_game_id(cursor, id)
    full_publisher = FullPublisherDAO().find_by_game_id(cursor, id)
    full_availables = FullAvailableDAO().find_by_game_id(cursor, id)

    if request.method == 'POST':
        text = request.form.get("text")
        score = request.form.get("score")

        user_review = ReviewDAO().filter_by_user_id_game_id(cursor, user_id=session['user_id'], game_id=id)
        if user_review:
            flash('Análise já publicada neste jogo.', category='error')
            return redirect(url_for('games.get_game', id=id))

        review = Review(user_id=session['user_id'], game_id=id, review_text=text, score=score, review_id=None, created_at=None)

        ReviewDAO().add(cursor, review)
        mysql.connection.commit()
        
        flash('Análise publicada.', category='success')
    
    full_reviews = FullReviewDAO().filter_by_game_id(cursor, id)

    return render_template("game.html", session=session, game=game, reviews=full_reviews, developer=full_developer, publisher=full_publisher, consoles=full_availables)

@games.route('/games/<int:id>/update', methods=['GET', 'POST'])
@is_authenticated
def update_game(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)
    game_available = AvailableDAO().find_by_game_id(cursor, id)

    developers = DeveloperDAO().get_all(cursor)
    publishers = PublisherDAO().get_all(cursor)
    consoles = ConsoleDAO().get_all(cursor)

    if request.method == 'POST':
        game_title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer_id = request.form.get('developer')
        publisher_id = request.form.get('publisher')
        trailer_url = request.form.get('trailer_url')
        console_ids = request.form.getlist('console')
        pic = request.files['pic']

        if not game_title:
            game_title = game.game_title
        if not release_date:
            release_date = game.release_date
        if not release_date:
            release_date = game.release_date
        if not description:
            description = game.description
        if not developer_id:
            developer_id = game.developer_id
        if not publisher_id:
            publisher_id = game.publisher_id
        if not trailer_url:
            trailer_url = game.trailer_url
        if pic:
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            image = Image(pic_id=None, data=pic.read(), mime_type=mimetype, file_name=filename, created_at=None)
            ImageDAO().add(cursor, image)
            mysql.connection.commit()
            cover_picture = cursor.lastrowid
        else:
            cover_picture = game.cover_picture

        if console_ids:
            availables_list = [a.console_id for a in game_available]

            for available in availables_list:
                if available not in console_ids:
                    delete_available = Available(game_id=game.game_id, console_id=available)
                    AvailableDAO().delete(cursor, delete_available)
                    mysql.connection.commit()

            for console_id in console_ids:
                if console_id not in availables_list:
                    add_available = Available(game_id=game.game_id, console_id=console_id)
                    AvailableDAO().add(cursor, add_available)
                    mysql.connection.commit()

        updated_game = Game(game_id=game.game_id, game_title=game_title, release_date=release_date, description=description, developer_id=developer_id, publisher_id=publisher_id, trailer_url=trailer_url, cover_picture=cover_picture)
        GameDAO().update(cursor, updated_game)
        mysql.connection.commit()

        flash('Jogo atualizado', category='success')
        return redirect(url_for('games.get_game', id=game.game_id))

    return render_template("update-game.html", session=session, game=game, developers=developers, publishers=publishers, consoles=consoles)

@games.route('/games/<int:id>/delete', methods=['GET', 'POST'])
@is_authenticated
def delete_game(id):
    if session['user_permission'] == "admin":
        try:
            print("indoooo")
            cursor = mysql.connection.cursor()
            GameDAO().delete(cursor, id)
            mysql.connection.commit()

            flash("Jogo excluído com sucesso", category="success")
            return redirect(url_for('games.get_games'))
        except:
            flash("Não foi possível excluir o jogo.", category="error")
            return redirect(url_for('games.get_games'))

    else:
        flash('Somente administradores podem remover jogos', category='error')
        return redirect(url_for('games.get_games', id=id))