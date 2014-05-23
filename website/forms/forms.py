#-*- coding:utf-8 -*-
from wtforms import Form, TextField, validators
import datetime
from website.models.models import Anime


class AddAnimeForm(Form):

    cn_name = TextField(U'中文名', [validators.Required()], id='cnname')
    name = TextField(U'原名', [validators.Required()], id='originname')
    tags = TextField(U'tags', [validators.Required()], id='tags')
    date = TextField(U'首映日期', [validators.Required()], id='date')
    finished = TextField(U'是否完结', [validators.Required()], id='finished')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        return True

    def set_anime(self):
        [year, month, day] = self.date.data.split(' ')[0].split('-')
        dt = datetime.date(int(year), int(month), int(day))
        user = Anime(cn_name=self.cn_name.data, name=self.name.data, first_time=dt, tags=self.tags.data,
                     finished=self.finished.data)
        return user


class EditAnimeForm(AddAnimeForm):

    def __init__(self, anime_id, **kwargs):
        self.anime_id = anime_id
        AddAnimeForm.__init__(self, **kwargs)

    def set_form_value(self):
        anime = self.get_anime()
        self.cn_name.data = anime.cn_name
        self.name.data = anime.name
        self.tags.data = anime.tags
        self.date.data = str(anime.first_time)
        self.finished.data = anime.finished

    def get_anime(self):
        anime = Anime.query.get(self.anime_id)
        return anime

    def update_anime(self):
        anime = self.get_anime()
        [year, month, day] = self.date.data.split(' ')[0].split('-')
        dt = datetime.date(int(year), int(month), int(day))
        anime.cn_name = self.cn_name.data
        anime.name = self.name.data
        anime.tags = self.tags.data
        anime.first_time = dt
        anime.finished = self.finished.data