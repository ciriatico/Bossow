from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.game_dao import Game, GameDAO
from website.models.review_dao import Review, ReviewDAO
from website.models.full_review_dao import FullReviewDAO

reviews = Blueprint('reviews', __name__)

@is_authenticated
@reviews.route('/delete-review', methods=['POST'])
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
@reviews.route('/reviews/<int:id>/update', methods=['GET', 'POST'])
def update_review(id):
    cursor = mysql.connection.cursor()
    review = ReviewDAO().find_by_id(cursor, id)
    game = GameDAO().find_by_id(cursor, review.game_id)

    if request.method == 'POST':
        if (review.user_id == session['user_id']) or (session['user_permission'] == "admin"):
            text = request.form.get("text")
            score = request.form.get("score")

            updated_text = review.review_text
            updated_score = review.score
            
            if text:
                updated_text = text
            if score:
                updated_score = score

            updated_review = Review(review_id=review.review_id, user_id=review.user_id, game_id=review.game_id, review_text=updated_text, score=updated_score, created_at=review.created_at)
            ReviewDAO().update(cursor, updated_review)
            mysql.connection.commit()
            flash('Análise atualizada', category='success')
            return redirect(url_for('games.get_game', id=game.game_id))
        else:
            flash('Não foi possível atualizar a análise', category='error')
            return redirect(url_for('games.get_game', id=game.game_id))

    return render_template("update-review.html", session=session, game=game)