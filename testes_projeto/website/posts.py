from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify
from flask_login import login_required, current_user
from .models import Game, Image, LibraryGame, Screenshot, Review, Complaint, User
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

@posts.route('/games', strict_slashes=False)
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

@login_required
@posts.route('/games/<int:id>/add-complaint', methods=['GET', 'POST'])
def add_complaint(id):
    if request.method == 'POST':
        game_id = id
        text = request.form.get('text')
        type = request.form.get('type')

        game = Game.query.filter_by(id=game_id).first()

        if game:
            complaint = Complaint(user_id=current_user.id, game_id=game_id, type=type, text=text)
            db.session.add(complaint)
            db.session.commit()
            flash('Problema relatado, aguarde a revisão do pedido.', category='success')
            return redirect(url_for('posts.games'))
        else:
            flash('Id fornecido não existe.', category='error')
            return redirect(url_for('posts.add_complaint'))

    return render_template('add-complaint.html', user=current_user, game_id=id)

@login_required
@posts.route('/complaints', methods=['GET', 'POST'], strict_slashes=False)
def complaints():
    complaints = Complaint.query.join(Game, Complaint.game_id == Game.id).add_columns(Game.title, Complaint.id, Complaint.game_id, Complaint.type, Complaint.text, Complaint.solved, Complaint.date_created).filter(Complaint.user_id == current_user.id)

    if request.method == 'POST':
        game_id = request.form.get('game_id')
        text = request.form.get('text')
        type = request.form.get('type')

        game = Game.query.filter_by(id=game_id).first()

        if game:
            complaint = Complaint(user_id=current_user.id, game_id=game_id, type=type, text=text)
            db.session.add(complaint)
            db.session.commit()
            flash('Problema relatado, aguarde a revisão do pedido.', category='success')
            return redirect(url_for('posts.games'))
        else:
            flash('Id fornecido não existe.', category='error')
            return redirect(url_for('posts.add_complaint'))

    return render_template('complaints.html', user=current_user, complaints=complaints)

@posts.route('/delete-complaint', methods=['POST'])
def delete_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if complaint.user_id == current_user.id:
            db.session.delete(complaint)
            db.session.commit()
    
    return jsonify({})

@login_required
@posts.route('/complaints/<int:id>/update', methods=['GET', 'POST'])
def update_complaint(id):
    complaint = Complaint.query.get(id)

    if request.method == 'POST':
        if complaint.user_id == current_user.id:
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

    return render_template("update-complaint.html", user=current_user)

@posts.route('/games/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_game(id):
    game = Game.query.get(id)

    if request.method == 'POST':
        title = request.form.get('title')
        release_date = request.form.get('release_date')
        description = request.form.get('description')
        developer = request.form.get('developer')
        publisher = request.form.get('publisher')
        trailer_url = request.form.get('trailer_url')
        pic = request.files['pic']

        if pic:
            old_img = Image.query.get(game.cover_picture)
            db.session.delete(old_img)

            filename = secure_filename(pic.filename)
            mimetype = pic.mimetype
            img = Image(img=pic.read(), mimetype=mimetype, name=filename)

            db.session.add(img)
            db.session.commit()

            game.cover_picture = img.id
        
        if title:
            game.title = title
        
        if release_date:
            game.release_date = release_date
        
        if description:
            game.description = description

        if developer:
            game.developer = developer
        
        if publisher:
            game.publisher = publisher
        
        if trailer_url:
            game.trailer_url = trailer_url

        db.session.commit()
        flash('Jogo atualizado', category='success')
        return redirect(url_for('posts.get_game', id=game.id))

    if current_user.role == "admin":
        return render_template("update-game.html", user=current_user, game_id=id)
    else:
        flash('Somente administradores podem alterar jogos', category='error')
        return redirect(url_for('posts.get_game', id=game.id))

@posts.route('/games/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_game(id):
    if current_user.role == "admin":
        game = Game.query.get(id)
        img = Image.query.get(game.cover_picture)

        try:
            db.session.delete(game)
            db.session.delete(img)
            db.session.commit()
            flash("Jogo excluído com sucesso", category="success")
            return redirect(url_for('posts.games'))
        except:
            flash("Não foi possível excluir o jogo.", category="error")
            return redirect(url_for('posts.games'))

    else:
        flash('Somente administradores podem remover jogos', category='error')
        return redirect(url_for('posts.games', id=game.id))

@posts.route('/profile/manage')
@login_required
def manage_profiles():
    if current_user.role == "admin":
        users = User.query.all()

        return render_template("profiles.html", user=current_user, users=users)
    else:
        flash('Somente administradores têm acesso à página de perfis', category='error')
        return redirect(url_for('views.dashboard'))

@posts.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def get_profile(id):
    profile = User.query.get(id)
    notes = profile.notes.all()
    reviews = profile.reviews.all()
    library_games = profile.library_games.all()
    complaints = profile.complaints.all()

    if request.method == 'POST':
        role = request.form.get('role')
        profile.role = role
        db.session.commit()

    return render_template("profile.html", user=current_user, profile=profile, reviews=reviews, complaints=complaints, library_games=library_games)

@posts.route('/complaints/manage')
@login_required
def manage_complaints():
    complaints = Complaint.query.all()

    return render_template("manage-complaints.html", user=current_user, complaints=complaints)

@posts.route('/check-complaint', methods=['POST'])
@login_required
def check_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if current_user.role == "admin":
            complaint.solved = True
            db.session.commit()
    
    return jsonify({})

@posts.route('/uncheck-complaint', methods=['POST'])
@login_required
def uncheck_complaint():
    data = json.loads(request.data)
    complaintId = data['complaintId']

    complaint = Complaint.query.get(complaintId)
    if complaint:
        if current_user.role == "admin":
            complaint.solved = False
            db.session.commit()
    
    return jsonify({})

@posts.route('/uploads/manage')
@login_required
def manage_uploads():
    uploads = Image.query.all()

    return render_template("manage-uploads.html", user=current_user, uploads=uploads)

@posts.route('/delete-upload', methods=['POST'])
@login_required
def delete_upload():
    data = json.loads(request.data)
    uploadId = data['uploadId']

    upload = Image.query.get(uploadId)
    db.session.delete(upload)
    db.session.commit()
    
    return jsonify({})