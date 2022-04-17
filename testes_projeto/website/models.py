from sqlalchemy import PrimaryKeyConstraint
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    profile_picture = db.Column(db.Integer, db.ForeignKey('image.id'))

    notes = db.relationship('Note', backref='user')
    reviews = db.relationship('Review', backref='user')
    library_games = db.relationship('LibraryGame', backref='user')

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    release_date = db.Column(db.String(150))
    description = db.Column(db.String(150))
    developer = db.Column(db.String(150))
    publisher = db.Column(db.String(150))
    trailer_url = db.Column(db.String(200))
    cover_picture = db.Column(db.Integer, db.ForeignKey('image.id'))

    reviews = db.relationship('Review', backref='game')
    library_games = db.relationship('LibraryGame', backref='game')

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    profile_pictures = db.relationship('User', backref='image')
    screenshots = db.relationship('Screenshot', backref='image')

class LibraryGame(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    spent_hours = db.Column(db.Integer)
    percentage_done = db.Column(db.Integer)
    last_logged = db.Column(db.Text)

class WishlistGame(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    date_added = db.Column(db.Date)

class Screenshot(db.Model):
    pic_id = db.Column(db.Integer, db.ForeignKey('image.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    text = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())