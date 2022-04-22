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
    role = db.Column(db.String(150), default="user")

    notes = db.relationship('Note', backref='user', lazy='dynamic')
    reviews = db.relationship('Review', backref='user', lazy='dynamic')
    library_games = db.relationship('LibraryGame', backref='user', lazy='dynamic')
    complaints = db.relationship('Complaint', backref='user', lazy='dynamic')

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
    complaints = db.relationship('Complaint', backref='game')

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

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    type = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    solved = db.Column(db.Boolean, nullable=False, default=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())