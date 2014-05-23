# -*- coding: utf8 -*-
import unittest
import datetime

from website import db
from website.models.models import User, Anime, Torrent, ActorQuote, AnimeReview


class TestModel(unittest.TestCase):
    def setUp(self):
        db.create_all()
        pass

    def tearDown(self):
        db.drop_all()
        pass


class TestAnime(TestModel):

    def test_create(self):
        assert len(Anime.query.all()) == 0
        Anime(cn_name=u'龙珠', tags='', finished=0, first_time=datetime.date.today(), name='').create()
        Anime(cn_name=u'虫师', tags='', finished=0, first_time=datetime.date(2014, 4, 4), name='').create()
        Anime(cn_name=u'JOJO', name=u'JOJO的奇妙冒险').create()
        assert len(Anime.query.all()) == 3

    def test_update(self):
        Anime(cn_name=u'龙珠', tags='', finished=0, first_time=datetime.date.today(), name='').create()
        t = Anime.query.all()[0]
        t.title = 'test'
        assert t.title == 'test'

    def test_delete(self):
        Anime(cn_name=u'虫师', tags='', finished=0, first_time=datetime.date(2014, 4, 4), name='').create()
        Anime(cn_name=u'JOJO', name=u'JOJO的奇妙冒险').create()
        ts = Anime.query.all()
        assert len(ts) == 2
        for t in ts:
            t.delete()
        assert len(Anime.query.all()) == 0

    def test_add_recommend(self):
        Anime(cn_name=u'JOJO', name=u'JOJO的奇妙冒险').create()
        anime = Anime.query.all()[0]
        actor_line = u'人被杀就会死'
        actor = u'卫宫士郎'
        anime.add_recommend(ActorQuote(actor_line=actor_line, actor_pic='', actor=actor))
        anime.add_recommend(AnimeReview(title='test1', link='http://test.com/1', summary='summarytest'))
        quote = ActorQuote.query.all()[0]
        review = AnimeReview.query.all()[0]
        assert quote.actor_line == actor_line
        assert quote.actor == actor
        assert review.title == 'test1'
        assert review.summary == 'summarytest'
        assert review.link == 'http://test.com/1'


class TestTorrent(TestModel):

    def test_create(self):
        assert len(Torrent.query.all()) == 0
        Torrent(title='title1', link='http://t.tt/link/1', enclosure='http://t.tt/1.torrent',
                pubdate=datetime.date(2014, 4, 4), description='').create()
        Torrent(title='title2', link='http://t.tt/link/2', enclosure='http://t.tt/2.torrent',
                pubdate=datetime.date.today(), description='').create()
        assert len(Torrent.query.all()) == 1

    def test_update(self):
        Torrent(title='', link='http://t.tt/link/1', enclosure='http://t.tt/1.torrent',
                pubdate=datetime.date(2014, 4, 4), description='').create()
        t = Torrent.query.all()[0]
        t.title = 'test'
        t.update()
        assert Torrent.query.all()[0].title == 'test'

    def test_delete(self):
        Torrent(title='title1', link='http://t.tt/link/1', enclosure='http://t.tt/1.torrent',
                pubdate=datetime.date(2014, 4, 4), description='').create()
        Torrent(title='title 2', link='http://t.tt/link/2', enclosure='http://t.tt/2.torrent',
                pubdate=datetime.date.today(), description='').create()
        ts = Torrent.query.all()
        assert len(ts) == 2
        for t in ts:
            t.delete()
        assert len(Torrent.query.all()) == 0


class TestQuote(TestModel):

    def test_create(self):
        Anime(cn_name=u'龙珠改', name=u'龙珠').create()
        assert len(ActorQuote.query.all()) == 0
        ActorQuote(anime_id=1, actor_line='', actor_pic='', actor='').create()
        assert len(ActorQuote.query.all()) > 0

    def test_update(self):
        Anime(cn_name=u'龙珠改', name=u'龙珠').create()
        ActorQuote(anime_id=1, actor_line='', actor_pic='', actor='').create()
        t = ActorQuote.query.all()[0]
        t.actor_line = 'test'
        assert t.actor_line == 'test'

    def test_delete(self):
        Anime(cn_name=u'龙珠改', name=u'龙珠').create()
        ActorQuote(anime_id=1, actor_line='', actor_pic='', actor='').create()
        ActorQuote(anime_id=1, actor_line='', actor_pic='', actor='').create()
        ts = ActorQuote.query.all()
        assert len(ts) == 2
        for t in ts:
            t.delete()
        assert len(ActorQuote.query.all()) == 0


class TestReview(TestModel):

    def test_create(self):
        Anime(cn_name=u'乒乓', name=u'乒乓').create()
        assert len(AnimeReview.query.all()) == 0
        AnimeReview(anime_id=1, title='test1', link='http://test.com/1', summary='').create()
        assert len(AnimeReview.query.all()) == 1

    def test_update(self):
        Anime(cn_name=u'乒乓', name=u'乒乓').create()
        AnimeReview(anime_id=1, title='test1', link='http://test.com/1', summary='').create()
        t = AnimeReview.query.all()[0]
        t.summary = 'test'
        assert t.summary == 'test'

    def test_delete(self):
        Anime(cn_name=u'乒乓', name=u'乒乓').create()
        AnimeReview(anime_id=1, title='test1', link='http://test.com/1', summary='').create()
        AnimeReview(anime_id=1, title='test2', link='http://test.org/2').create()
        ts = AnimeReview.query.all()
        assert len(ts) == 2
        for t in ts:
            t.delete()
        assert len(AnimeReview.query.all()) == 0


class TestUser(TestModel):

    def test_register(self):
        user = User(nickname='kxxoling', openid='', google_account='kxxoling@gmail.com')
        user.register()
        assert User.query.filter_by(nickname='kxxoling')[0] is not None

    def test_update(self):
        user = User(nickname='kxxoling', openid='', google_account='kxxoling@gmail.com')
        user.register()
        user.update()
        assert User.query.filter_by(nickname='kxxoling')[0] is not None

    def test_delete(self):
        user = User(nickname='kxxoling', openid='', google_account='kxxoling@gmail.com')
        user.register()
        for user in User.query.all():
            user.delete()
        assert len(User.query.all()) == 0

    def test_update_role(self):
        user = User(nickname='kxxoling', openid='', google_account='kxxoling@gmail.com')
        user.register()
        user.update_role(3)
        role2 = User.query.filter_by(nickname='kxxoling')[0].role
        assert role2 == 3

    def test_like(self):
        User(nickname='kxxoling', openid='', google_account='kxxoling@gmail.com').register()
        Anime(cn_name=u'JOJO', name=u'JOJO的奇妙冒险').create()
        anime = Anime.query.all()[0]
        anime.add_recommend(ActorQuote(anime_id=1, actor_line='', actor_pic='', actor=''))
        user = User.query.all()[0]
        quote = ActorQuote.query.all()[0]
        user.like(quote)
        assert ActorQuote.query.all()[0].likes == 1


if __name__ == '__main__':
    unittest.main()