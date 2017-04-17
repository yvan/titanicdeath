import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ['FLASK_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    APP_STATIC = os.path.join(APP_ROOT, 'static')

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

'''
    author @yvan
    configuration file for flask
    put sensitive info in instance/config.py
    read https://exploreflask.com/configuration.html
    read http://flask.pocoo.org/docs/0.10/config/
'''