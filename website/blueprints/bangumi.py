# -*- coding: utf8 -*-
import datetime

from flask import render_template, Blueprint

from website import app
from website.models.models import Anime, Torrent


bangumi_bp = Blueprint('bangumi', __name__, url_prefix='/animes', template_folder='../templates/bangumi')


@bangumi_bp.route('/')
@bangumi_bp.route('/today/')
def show_animes_today():
    now = datetime.date.today()
    this_year = now.year
    this_season = now.month/3 + 1
    weekday = now.weekday()
    animes = Anime.query.filter_by(year=this_year, season=this_season, weekday=weekday)
    torrents = {anime.cn_name: Torrent.query.filter_by(anime.like('%'+anime.cn_name+'%')) for anime in animes}
    return render_template('today.html', animes=animes, torrents=torrents)


@bangumi_bp.route('/season/')
def show_animes_this_season():
    [monday, tuesday, wednesday, thursday, friday, saturday, sunday] = \
        [Anime.query.filter_by(year=2014, season=2, weekday=i)
         for i in range(7)]
    return render_template('season.html', monday=monday, tuesday=tuesday, wednesday=wednesday,
                           thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)


@bangumi_bp.route('/all/')
@bangumi_bp.route('/all/<int:page>/')
def show_all_animes(page=1):
    animes = Anime.query.paginate(page, app.config['ANIMES_PER_PAGE'], False).items
    return render_template('all.html', animes=animes)