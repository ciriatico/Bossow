from website import app, mysql
from platform import release
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response, jsonify, session
import json
import datetime
from werkzeug.utils import secure_filename
from website.decorators.auth import is_authenticated, has_permission
from website.models.review_dao import Review, ReviewDAO
from website.models.library_dao import Library, LibraryDAO
from website.models.user_dao import User, UserDAO
from website.models.complaint_dao import Complaint, ComplaintDAO
from website.models.full_complaint_dao import FullComplaintDAO
from website.models.ranking_dao import RankingDAO

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", session=session)

@views.route('/ranking')
def get_ranking():
    cursor = mysql.connection.cursor()
    ranking = RankingDAO().get_all(cursor)

    return render_template("ranking.html", session=session, rankings=ranking)

@views.route('/dashboard', methods=['POST', 'GET'])
@is_authenticated
def dashboard():
    cursor = mysql.connection.cursor()

    if session['user_permission'] == "admin":
        users = UserDAO().get_all(cursor)
        complaints = ComplaintDAO().get_all(cursor)

        admin_info_dict = {
            "users": len(users),
            "unsolved_complaints": len([c for c in complaints if not c.solved])
        }
    else:
        admin_info_dict = dict()

    user = UserDAO().find_by_id(cursor, session['user_id'])
    library_games = LibraryDAO().filter_by_user_id(cursor, session['user_id'])
    reviews = ReviewDAO().filter_by_user_id(cursor, session['user_id'])
    complaints = ComplaintDAO().filter_by_user_id(cursor, session['user_id'])
    complaints_solved = [c.solved for c in complaints]
    complaints_solved_dict = {
        "solved": sum(complaints_solved),
        "unsolved": len(complaints_solved) - sum(complaints_solved)
    }

    return render_template("dashboard.html", session=session, user=user, library_games=library_games, reviews=reviews, complaints_solved=complaints_solved_dict, admin_info=admin_info_dict)