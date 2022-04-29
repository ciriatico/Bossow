from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
from flask_login import login_required, current_user
from .models import Game, Image, LibraryGame, Screenshot, Review, Complaint, User
from . import db
import json
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models_p.full_library_game_dao import FullLibraryGame, FullLibraryGameDAO
from website.models_p.image_dao import Image, ImageDAO
from website.models_p.game_dao import GameDAO
from website.models_p.review_dao import ReviewDAO
from website.models_p.full_review_dao import FullReviewDAO
from website.models_p.library_game_dao import LibraryGame, LibraryGameDAO
from website.models_p.screenshot_dao import Screenshot, ScreenshotDAO
from website.models_p.note_dao import NoteDAO
from website.models_p.user_dao import UserDAO
from website.models_p.complaint_dao import ComplaintDAO
from website.models_p.full_complaint_dao import FullComplaintDAO
import datetime

posts = Blueprint('posts', __name__)

@posts.route('/games', strict_slashes=False)
def games():
    cursor = mysql.connection.cursor()
    games = GameDAO().get_all_sorted(cursor, 'release_date')
    return render_template("games.html", games=games, session=session)

@is_authenticated
@posts.route('/add-game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer = request.form.get('developer')
        publisher = request.form.get('publisher')
        trailer_url = request.form.get('trailer_url')

        print(f"release_date {type(release_date)}")

        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype

        cursor = mysql.connection.cursor()
        img = Image(id=None, img=pic.read(), mimetype=mimetype, filename=filename, created_at=None)
        ImageDAO().add(cursor, img)
        mysql.connection.commit()
        cover_picture = cursor.lastrowid

        add_game = Game(title=title, release_date=release_date, description=description, developer=developer, publisher=publisher, trailer_url=trailer_url, cover_picture=cover_picture)
        GameDAO().add(cursor, add_game)
        mysql.connection.commit()
        
        flash('Jogo adicionado!', category='success')
        return redirect(url_for('posts.games'))

    return render_template('add-game.html', session=session)

# @posts.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         pic = request.files['pic']

#         if not pic:
#             return 'No pic uploaded.'

#         filename = secure_filename(pic.filename)
#         mimetype = pic.mimetype
#         img = Image(img=pic.read(), mimetype=mimetype, name=filename)
#         db.session.add(img)
#         db.session.commit()
#         flash('Imagem adicionada com sucesso', category='success')

#     return render_template("upload.html", session=session)

@posts.route('/image')
def get_image_page():
    return render_template("image.html", session=session)

@posts.route('/image/<int:id>')
def get_image(id):
    cursor = mysql.connection.cursor()
    img = ImageDAO().find_by_id(cursor, id)
    if not img:
        return redirect(url_for('views.home'))

    return Response(img.img, mimetype=img.mimetype)

@posts.route('/games/<int:id>', methods=['GET', 'POST'])
def get_game(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        text = request.form.get("text")
        score = request.form.get("score")

        review = Review(user_id=session['user_id'], game_id=id, text=text, score=score)

        ReviewDAO().add(cursor, review)
        mysql.connection.commit()
        
        flash('Análise publicada.', category='success')
    
    full_reviews = FullReviewDAO().filter_by_game_id(cursor, id)

    return render_template("game.html", session=session, game=game, reviews=full_reviews)

@posts.route('/add-to-library', methods=['POST'])
def add_to_library():
    data = json.loads(request.data)
    gameId = data['gameId']

    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, gameId)
    library_games = LibraryGameDAO().filter_by_user_id(cursor, session['user_id'])

    games_in_library = [r.game_id for r in library_games]

    if gameId in games_in_library:
        flash("Jogo já está na sua biblioteca.", category="error")
    elif game:
        game_to_user = LibraryGame(user_id=session['user_id'], game_id=gameId)
        LibraryGameDAO().add(cursor, game_to_user)
        mysql.connection.commit()
        flash("Jogo adicionado com sucesso à sua biblioteca!", category="success")
    
    return jsonify({})

@is_authenticated
@posts.route('/library')
def library():
    cursor = mysql.connection.cursor()
    full_library_games = FullLibraryGameDAO().find_by_user_id(cursor, session['user_id'])

    return render_template("library.html", session=session, games=full_library_games)

@is_authenticated
@posts.route('/library/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def get_game_in_library(id):
    cursor = mysql.connection.cursor()
    library_game = LibraryGameDAO().filter_by_user_id_game_id(cursor, session['user_id'], id)
    game = GameDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype

        cursor = mysql.connection.cursor()
        img = Image(id=None, img=pic.read(), mimetype=mimetype, filename=filename, created_at=None)
        ImageDAO().add(cursor, img)
        mysql.connection.commit()

        screenshot = Screenshot(pic_id=cursor.lastrowid, user_id=session['user_id'], game_id=id)
        ScreenshotDAO().add(cursor, screenshot)
        mysql.connection.commit()

    screenshots = ScreenshotDAO().filter_by_user_id_game_id(cursor, session['user_id'], id)

    return render_template("library_game.html", session=session, library_game=library_game, game=game, screenshots=screenshots)


@is_authenticated
@posts.route('/library/<int:id>/delete')
def delete_from_library(id):
    cursor = mysql.connection.cursor()
    LibraryGameDAO().delete(cursor, session['user_id'], id)
    mysql.connection.commit()

    flash('Jogo removido da biblioteca', category='success')

    return redirect(url_for('posts.library'))

@is_authenticated
@posts.route('/library/<int:id>/update', methods=['GET', 'POST'])
def update_library(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        library_game = LibraryGameDAO().filter_by_user_id_game_id(cursor, session['user_id'], id)

        hours_played = request.form.get('hours_played')
        completion_percentage = request.form.get('completion_percentage')
        last_logged_in = request.form.get('last_logged_in')

        if not hours_played:
            hours_played = library_game.hours_played
        if not completion_percentage:
            completion_percentage = library_game.completion_percentage
        if not last_logged_in:
            last_logged_in = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:00")
        
        updated_library_game = LibraryGame(library_game.user_id, library_game.game_id, hours_played, completion_percentage, last_logged_in)
        LibraryGameDAO().update(cursor, updated_library_game)
        mysql.connection.commit()

        flash('Dados atualizados!', category='success')
        return redirect(url_for('posts.get_game_in_library', id=game.id))

    return render_template("update-library.html", session=session, game=game)

@posts.route('/delete-review', methods=['POST'])
def delete_review():
    data = json.loads(request.data)
    reviewId = data['reviewId']
    
    cursor = mysql.connection.cursor()
    review = ReviewDAO().find_by_id(cursor, reviewId)
    
    if review:
        if review.user_id == session['user_id'] or session['user_permission'] == "admin":

            cursor = mysql.connection.cursor()
            ReviewDAO().delete(cursor, session['user_id'], reviewId)
            mysql.connection.commit()

            flash("Review excluído com sucesso!", category="success")
    
    return jsonify({})

@is_authenticated
@posts.route('/games/<int:id>/add-complaint', methods=['GET', 'POST'])
def add_complaint(id):
    if request.method == 'POST':
        game_id = id
        text = request.form.get('text')
        type = request.form.get('type')

        game = Game.query.filter_by(id=game_id).first()

        if game:
            complaint = Complaint(user_id=session['user_id'], game_id=game_id, type=type, text=text)
            db.session.add(complaint)
            db.session.commit()
            flash('Problema relatado, aguarde a revisão do pedido.', category='success')
            return redirect(url_for('posts.games'))
        else:
            flash('Id fornecido não existe.', category='error')
            return redirect(url_for('posts.add_complaint'))

    return render_template('add-complaint.html', session=session, game_id=id)

@posts.route('/complaints', methods=['GET', 'POST'], strict_slashes=False)
@is_authenticated
def complaints():
    cursor = mysql.connection.cursor()
    full_complaints = FullComplaintDAO().filter_by_user_id(cursor, session['user_id'])

    if request.method == 'POST':
        game_id = request.form.get('game_id')
        text = request.form.get('text')
        type = request.form.get('type')

        game = Game.query.filter_by(id=game_id).first()

        if game:
            complaint = Complaint(user_id=session['user_id'], game_id=game_id, type=type, text=text)
            db.session.add(complaint)
            db.session.commit()
            flash('Problema relatado, aguarde a revisão do pedido.', category='success')
            return redirect(url_for('posts.games'))
        else:
            flash('Id fornecido não existe.', category='error')
            return redirect(url_for('posts.add_complaint'))

    return render_template('complaints.html', session=session, complaints=full_complaints)

@posts.route('/delete-complaint', methods=['POST'])
def delete_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if complaint.user_id == session['user_id']:
            db.session.delete(complaint)
            db.session.commit()
    
    return jsonify({})

@is_authenticated
@posts.route('/complaints/<int:id>/update', methods=['GET', 'POST'])
def update_complaint(id):
    complaint = Complaint.query.get(id)

    if request.method == 'POST':
        if complaint.user_id == session['user_id']:
            game_id = request.form.get('game_id')
            text = request.form.get('text')
            type = request.form.get('type')

            if game_id:
                game = Game.query.get(game_id)

                if not game:
                    flash('Id de jogo não existe dado não existe', category='error')
                    return redirect(url_for('posts.update_complaint', id=complaint.id))
                else:
                    complaint.game_id = game_id
            
            if text:
                complaint.text = text
            
            if type:
                complaint.type = type
            
            db.session.commit()
            flash('Denúncia atualizada', category='success')
            return redirect(url_for('posts.complaints'))
        else:
            flash('Denúncia pedida não foi feita pelo usuário conectado', category='error')
            return redirect(url_for('posts.complaints'))

    return render_template("update-complaint.html", session=session)


@posts.route('/games/<int:id>/update', methods=['GET', 'POST'])
@is_authenticated
def update_game(id):
    cursor = mysql.connection.cursor()
    game = GameDAO().find_by_id(cursor, id)

    if request.method == 'POST':
        title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer = request.form.get('developer')
        publisher = request.form.get('publisher')
        trailer_url = request.form.get('trailer_url')
        pic = request.files['pic']

        if not title:
            title = game.title
        if not release_date:
            release_date = game.release_date
        if not release_date:
            release_date = game.release_date
        if not description:
            description = game.description
        if not developer:
            developer = game.developer
        if not publisher:
            publisher = game.publisher
        if not trailer_url:
            trailer_url = game.trailer_url
        if pic:
            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            img = Image(id=None, img=pic.read(), mimetype=mimetype, filename=filename, created_at=None)
            ImageDAO().add(cursor, img)
            mysql.connection.commit()
            cover_picture = cursor.lastrowid
        else:
            cover_picture = game.cover_picture

        updated_game = Game(id=game.id, title=title, release_date=release_date, description=description, developer=developer, publisher=publisher, trailer_url=trailer_url, cover_picture=cover_picture)
        
        GameDAO().update(cursor, updated_game)
        mysql.connection.commit()

        flash('Jogo atualizado', category='success')
        return redirect(url_for('posts.get_game', id=game.id))

    return render_template("update-game.html", session=session, game_id=id)


@posts.route('/games/<int:id>/delete', methods=['GET', 'POST'])
@is_authenticated
def delete_game(id):
    if session['user_permission'] == "admin":
        try:
            cursor = mysql.connection.cursor()
            GameDAO().delete(cursor, session['user_id'], id)
            mysql.connection.commit()

            flash("Jogo excluído com sucesso", category="success")
            return redirect(url_for('posts.games'))
        except:
            flash("Não foi possível excluir o jogo.", category="error")
            return redirect(url_for('posts.games'))

    else:
        flash('Somente administradores podem remover jogos', category='error')
        return redirect(url_for('posts.games', id=id))

@posts.route('/profile/manage')
@is_authenticated
@has_permission("admin")
def manage_profiles():
    cursor = mysql.connection.cursor()
    users = UserDAO().get_all(cursor)
    return render_template("profiles.html", session=session, users=users)

@posts.route('/profile/<int:id>', methods=['GET', 'POST'])
@is_authenticated
def get_profile(id):
    cursor = mysql.connection.cursor()

    profile = UserDAO().find_by_id(cursor, id)
    notes = NoteDAO().filter_by_user_id(cursor, id)
    full_reviews = FullReviewDAO().find_by_user_id(cursor, id)
    print(f"full_reviews {full_reviews}")
    full_library_games = FullLibraryGameDAO().find_by_user_id(cursor, id)
    print(f"full_library_games {full_library_games}")
    complaints = ComplaintDAO().filter_by_user_id(cursor, id)

    if request.method == 'POST':
        role = request.form.get('role')
        profile.role = role
        db.session.commit()

    return render_template("profile.html", session=session, profile=profile, reviews=full_reviews, complaints=complaints, library_games=full_library_games)

@posts.route('/complaints/manage')
@is_authenticated
@has_permission('admin')
def manage_complaints():
    cursor = mysql.connection.cursor()
    full_complaints = FullComplaintDAO().get_all(cursor)

    return render_template("manage-complaints.html", session=session, complaints=full_complaints)

@posts.route('/check-complaint', methods=['POST'])
@is_authenticated
def check_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if session['user_permission'] == "admin":
            complaint.solved = True
            db.session.commit()
    
    return jsonify({})

@posts.route('/uncheck-complaint', methods=['POST'])
@is_authenticated
def uncheck_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if session['user_permission'] == "admin":
            complaint.solved = False
            db.session.commit()
    
    return jsonify({})

@posts.route('/uploads/manage')
@is_authenticated
@has_permission('admin')
def manage_uploads():
    cursor = mysql.connection.cursor()
    uploads = ImageDAO().get_all(cursor)

    return render_template("manage-uploads.html", session=session, uploads=uploads)

@posts.route('/delete-screenshot', methods=['POST'])
@is_authenticated
def delete_screenshot():
    data = json.loads(request.data)
    uploadId = data['uploadId']

    cursor = mysql.connection.cursor()
    ImageDAO().delete(cursor, uploadId)
    mysql.connection.commit()

    flash('Captura de tela deletada com sucesso!', category='success')
    
    return jsonify({})

@posts.route('/delete-upload', methods=['POST'])
@is_authenticated
def delete_upload():
    data = json.loads(request.data)
    uploadId = data['uploadId']

    cursor = mysql.connection.cursor()
    ImageDAO().delete(cursor, uploadId)
    mysql.connection.commit()
    
    return jsonify({})