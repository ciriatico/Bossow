from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.full_library_dao import FullLibrary, FullLibraryDAO
from website.models.image_dao import Image, ImageDAO
from website.models.game_dao import Game, GameDAO
from website.models.library_dao import Library, LibraryDAO
from website.models.screenshot_dao import Screenshot, ScreenshotDAO

library = Blueprint('library', __name__)

@is_authenticated
@library.route('/add-to-library', methods=['POST'])
def add_to_library():
    data = json.loads(request.data)
    gameId = data['gameId']

    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, gameId)
    library_games = LibraryDAO().filter_by_user_id(cursor, session['user_id'])

    games_in_library = [r.game_id for r in library_games]

    if gameId in games_in_library:
        flash("Jogo já está na sua biblioteca.", category="error")
    elif game:
        game_to_user = Library(user_id=session['user_id'], game_id=gameId)
        LibraryDAO().add(cursor, game_to_user)
        mysql.connection.commit()
        flash("Jogo adicionado com sucesso à sua biblioteca!", category="success")
    
    return jsonify({})

@is_authenticated
@library.route('/library')
def get_library():
    cursor = mysql.connection.cursor()
    full_library_games = FullLibraryDAO().find_by_user_id(cursor, session['user_id'])

    return render_template("library.html", session=session, games=full_library_games)

@is_authenticated
@library.route('/library/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def get_game_in_library(id):
    cursor = mysql.connection.cursor()
    library_game = LibraryDAO().filter_by_user_id_game_id(cursor, user_id=session['user_id'], game_id=id)
    game = GameDAO().find_by_id(cursor, id)

    print("dasdas")
    print(library_game.user_id)

    if request.method == 'POST':
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype

        cursor = mysql.connection.cursor()
        image = Image(pic_id=None, data=pic.read(), mime_type=mimetype, file_name=filename, created_at=None)
        ImageDAO().add(cursor, image)
        mysql.connection.commit()

        screenshot = Screenshot(pic_id=cursor.lastrowid, user_id=session['user_id'], game_id=id)
        ScreenshotDAO().add(cursor, screenshot)
        mysql.connection.commit()

    screenshots = ScreenshotDAO().filter_by_user_id_game_id(cursor, session['user_id'], id)

    return render_template("library_game.html", session=session, library_game=library_game, game=game, screenshots=screenshots)

@is_authenticated
@library.route('/library/<int:id>/delete')
def delete_from_library(id):
    cursor = mysql.connection.cursor()
    LibraryDAO().delete(cursor, session['user_id'], id)
    mysql.connection.commit()

    flash('Jogo removido da biblioteca', category='success')

    return redirect(url_for('library.get_library'))

@is_authenticated
@library.route('/library/<int:id>/update', methods=['GET', 'POST'])
def update_library(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        library_game = LibraryDAO().filter_by_user_id_game_id(cursor, session['user_id'], id)

        hours_played = request.form.get('hours_played')
        completion_percentage = request.form.get('completion_percentage')
        last_logged_in = request.form.get('last_logged_in')

        if not hours_played:
            hours_played = library_game.hours_played
        if not completion_percentage:
            completion_percentage = library_game.completion_percentage
        if not last_logged_in:
            last_logged_in = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:00")
        
        updated_library_game = Library(library_game.user_id, library_game.game_id, hours_played, completion_percentage, last_logged_in)
        LibraryDAO().update(cursor, updated_library_game)
        mysql.connection.commit()

        flash('Dados atualizados!', category='success')
        return redirect(url_for('games.get_game_in_library', id=game.game_id))

    return render_template("update-library.html", session=session, game=game)