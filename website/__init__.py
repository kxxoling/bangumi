# -*- coding: utf8 -*-
from functools import wraps

from flask import Flask, Blueprint, session, g, flash, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.openid import OpenID


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
oid = OpenID(app, '/var/tmp')


@app.before_request
def lookup_current_user():
    g.user = None
    if 'user_id' in session:
        user_id = session['user_id']
        g.user = User.query.get(user_id)
        if not g.user:
            session.clear('user_id')


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user:
            flash('You must login to visit this page!')
            return redirect(url_for('index.login'))
        return func(*args, **kwargs)
    return wrapper


def get_right_side_bar(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        anime = Anime(cn_name=u'物语系列')
        anime.id = 2
        g.newest_added_animes = [anime]
        g.newest_updated_animes = []
        return func(*args, **kwargs)
    return wrapper


from website.models.models import User, Anime, Torrent, AnimeReview, ActorQuote
from website.blueprints.index import index_bp
from website.blueprints.anime import anime_bp
from website.blueprints.bangumi import bangumi_bp
from website.blueprints.admin import admin

app.register_blueprint(index_bp)
app.register_blueprint(anime_bp)
app.register_blueprint(bangumi_bp)

db.create_all()