# -*- coding: utf8 -*-
from website import db
import datetime


FINISHED = 1
NOT_FINISHED = 0


class CURDMixIN():
    """提供基本的 CURD 支持，操作成功返回 True，失败则回滚事物，返回 False"""
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print e
            db.session.rollback()
            return False
        return True

    def update(self):
        try:
            db.session.commit()
        except Exception as e:
            print e
            db.session.rollback()
            return False
        return True

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print e
            db.session.rollback()
            return False
        return True


class Anime(db.Model, CURDMixIN):
    __tablename__ = 'animes'

    id = db.Column(db.Integer, primary_key=True)        # 主键
    cn_name = db.Column(db.String(100), unique=True)    # 作品名
    name = db.Column(db.String(100), unique=True)       # 作品搜索用名称
    year = db.Column(db.Integer)                        # 创作年份（首年）
    season = db.Column(db.String(20))                   # 季度（1，2，3，4 分别表示 1，4，7，10 月份开始的冬、春、夏、秋季番
    weekday = db.Column(db.Integer)                     # 播放日期星期几
    tags = db.Column(db.String(100))                    # 标签
    first_time = db.Column(db.DateTime)                 # 首播日期
    finished = db.Column(db.Integer)                    # 是否完结

    def __init__(self, cn_name, tags='', finished=0, first_time=datetime.date.today(), name=''):
        self.cn_name = cn_name
        self.name = name or cn_name
        self.first_time = first_time or datetime.date.today()
        self.year = first_time.year
        self.season = first_time.month/3 + 1
        self.weekday = first_time.weekday()
        self.tags = tags or (self.cn_name + ',' + self.name)
        self.finished = finished or NOT_FINISHED

    def add_recommend(self, something):
        """新增推荐，something 可以是 ActorQuote 或者 AnimeReview"""
        something.anime_id = self.id
        something.create()

    def is_finished(self):
        return self.finshed and False or True

    def finish(self):
        self.finished = FINISHED
        return self

    def unfinished(self):
        self.finished = NOT_FINISHED

    def get_alike_torrents(self, lmt):
        return Torrent.query.filter(Torrent.title.like('%'+self.name+'%')).limit(lmt)

    @classmethod
    def get_newest_added(cls, lmt):
        return cls.query.order_by(cls.id.desc()).limit(lmt)

    @classmethod
    def get_newest_updated(cls, lmt):
        """__TODO__: 暂时以最近添加代替"""
        return cls.get_newest_added(lmt)

    def __repr__(self):
        return (u'''
        Bangumi id: %s
        Chinese Name: %s
        Original Name: %s
        Finished or Not: %s''' % (self.id, self.cn_name, self.name, self.finished)).encode('utf-8')


class Torrent(db.Model, CURDMixIN):
    __tablename__ = "torrents"

    id = db.Column(db.Integer, primary_key=True)            # 主键
    title = db.Column(db.String(200))                       # 种子标题
    link = db.Column(db.String(200), unique=True)           # 外站链接
    enclosure = db.Column(db.String(100), unique=True)      # 附件链接
    pub_date = db.Column(db.DateTime)                       # 发布日期
    description = db.Column(db.String(1000))                # 介绍

    def __init__(self, title, link, enclosure='', pubdate=datetime.datetime.now(), description=''):
        self.title = title
        self.link = link
        self.enclosure = enclosure
        self.pub_date = pubdate
        self.description = description

    def __repr__(self):
        return (u'''
        Torrent id: %s
        Title: %s
        Link: %s''' % (self.id, self.title, self.link)).encode('utf-8')


class User(db.Model, CURDMixIN):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)                # 主键
    google_account = db.Column(db.String(50), unique=True)      # GMail 邮箱
    openid = db.Column(db.String(100))                          # openid 链接
    nickname = db.Column(db.String(50), unique=True)            # 昵称/用户名
    register_time = db.Column(db.DateTime)                      # 注册日期
    role = db.Column(db.Integer)                                # 角色

    def __init__(self, nickname, openid, google_account):
        self.register_time = datetime.datetime.now()
        self.nickname = nickname
        self.openid = openid
        self.google_account = google_account
        self.role = 0

    def register(self):
        return self.create()

    def update_role(self, role):
        self.role = role
        return self.update()

    def like(self, something):
        """新增推荐，something 可以是 ActorQuote 或者 AnimeReview"""
        something.likes += 1
        something.update()

    def approve(self):
        """审核通过，审核目标暂时考虑为新用户/ActorQuote/AnimeReview，限定审核权限"""
        pass

    def __repr__(self):
        return (u'''
        User id: %s
        Nick Name: %s
        E-Mail: %s''' % (self.id, self.nickname, self.google_account)).encode('utf-8')


class ActorQuote(db.Model, CURDMixIN):
    __tablename__ = 'actor_lines'

    id = db.Column(db.Integer, primary_key=True)                    # 主键
    actor_line = db.Column(db.String(400))                          # 台词内容
    anime_id = db.Column(db.Integer, db.ForeignKey('animes.id'))    # 相关动画 id
    actor_pic = db.Column(db.Text)                                  # 角色头像图片链接/base64 编码
    actor = db.Column(db.String(20))                                # 角色名
    likes = db.Column(db.Integer, default=0)                        # 点赞数

    def __init__(self, actor_line, anime_id=None, actor_pic='', actor=''):
        self.anime_id = anime_id
        self.actor_line = actor_line
        self.actor_pic = actor_pic
        self.actor = actor


class AnimeReview(db.Model, CURDMixIN):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)                    # 主键
    title = db.Column(db.String(50))                                # 漫评标题
    link = db.Column(db.String(100))                                # 漫评链接
    summary = db.Column(db.String(1000))                            # 漫评概要
    anime_id = db.Column(db.Integer, db.ForeignKey('animes.id'))    # 相关动画 id
    likes = db.Column(db.Integer, default=0)                        # 点赞数

    def __init__(self, title, link, anime_id=None, summary=''):
        self.anime_id = anime_id
        self.title = title
        self.link = link
        self.summary = summary