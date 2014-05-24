# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, Blueprint

from website import app, db, login_required, get_right_side_bar
from website.models.models import Anime, Torrent
from website.forms.forms import AddAnimeForm, EditAnimeForm


anime_bp = Blueprint('anime', __name__, url_prefix='/anime', template_folder='../templates/anime')


@anime_bp.route('/')
def anime():
    return redirect(url_for('index.index'))


@anime_bp.route('/<int:anime_id>/')
@get_right_side_bar
def show_anime(anime_id):
    anime = Anime.query.get(anime_id)
    torrents = anime.get_alike_torrents()
    return render_template('anime.html', anime=anime, torrents=torrents)


@anime_bp.route('/add/', methods=['POST', 'GET'])
@login_required
def add_anime():
    form = AddAnimeForm(request.form)
    if request.method == 'GET':
        return render_template('add.html', form=form)
    if request.method == 'POST' and form.validate():
        print form.cn_name.dat
        db.session.add(form.set_anime())
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(e)
            flash('Add anime failed!')
        else:
            flash('Successfully added an anime!')
        return redirect(url_for('show_anime'))


@anime_bp.route('/edit/<int:anime_id>/', methods=['POST', 'GET'])
@login_required
def edit_anime(anime_id):
    form = EditAnimeForm(anime_id, formdata=request.form)
    if request.method == 'GET':
        if form.get_anime() is None:
            return 'ERROR 404: PAGE NOT FOUND!', 404
        else:
            form.set_form_value()
            return render_template('edit.html', form=form)
    if request.method == 'POST' and form.validate():
        form.update_anime()
        try:
            db.session.commit()
        except Exception as e:
            flash('Edit anime failed!')
        else:
            flash('Edit successfully finished!')
        return redirect(url_for('show_anime', anime_id=anime_id))


@anime_bp.route('/search/')
@get_right_side_bar
def search():
    if request.args.get('q'):
        info = request.args['q']
        try:
            anime_id = int(info)
            return redirect(url_for('.show_anime', anime_id=anime_id))
        except ValueError:
            animes = Anime.get_alike_animes(info)
            return render_template('search.html', animes=animes)
    else:
        flash('You need to type something to search!')
        return redirect(url_for('index.index'))
