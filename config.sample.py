import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
ANIMES_PER_PAGE = 10
LOGGING_DIR = os.path.join(BASE_DIR, 'log')