from flask import Flask
from os import path
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Vida querida'
mysql = MySQL(app)

from website.controllers.complaints import complaints
from website.controllers.games import games
from website.controllers.images import images
from website.controllers.library import library
from website.controllers.notes import notes
from website.controllers.profiles import profiles
from website.controllers.reviews import reviews
from website.controllers.views import views

app.register_blueprint(complaints, url_prefix='/')
app.register_blueprint(games, url_prefix='/')
app.register_blueprint(images, url_prefix='/')
app.register_blueprint(library, url_prefix='/')
app.register_blueprint(notes, url_prefix='/')
app.register_blueprint(profiles, url_prefix='/')
app.register_blueprint(reviews, url_prefix='/')
app.register_blueprint(views, url_prefix='/')