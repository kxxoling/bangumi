from functools import wraps

from flask import session, flash, url_for, g, redirect, render_template, request, Blueprint

from website.models.models import User
from website import oid


index_bp = Blueprint('index', __name__, template_folder='../templates/index')

@oid.after_login
def create_or_login(resp):
    user = User.query.filter_by(google_account=resp.email).first()
    if user is None:
        user = User(nickname=resp.nickname or resp.fullname, google_account=resp.email,
                    openid=resp.identity_url)
        if user.register():
            flash(u"You've successfully registered and signed in!")
        else:
            flash(u'Register failed!')
            return redirect(oid.get_next_url())
    else:
        flash("You've successfully logged in!")
    session['user_id'] = user.id
    g.user = user
    return redirect(oid.get_next_url())


@index_bp.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if session.get('user_id'):
        flash("You've logged in!")
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.form.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['email', 'nickname', 'fullname'])
    return render_template('login.html', next=oid.get_next_url(),
                           error=oid.fetch_error())


@index_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('nickname')
    flash(u'You were signed out')
    return redirect(oid.get_next_url())


@index_bp.route('/')
def index():
    return render_template('hello.html')