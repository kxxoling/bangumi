# -*- coding: utf8 -*-
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin
from flask import g
from website import app, db
from website.models.models import User, Anime, Torrent, AnimeReview, ActorQuote


class AdminRequiredView(ModelView):

    def is_accessible(self):
        if g.user:
            return g.user.is_admin()
        return False


class LoginRequiredView(ModelView):

    def is_accessible(self):
        if g.user:
            return True
        return False


admin = Admin(app)
admin.add_view(AdminRequiredView(User, db.session))
admin.add_view(ModelView(Anime, db.session))
admin.add_view(ModelView(Torrent, db.session))

