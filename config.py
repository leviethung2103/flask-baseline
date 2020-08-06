from os import environ, path
from dotenv import load_dotenv
import os
from utils.helpers import export_routes, export_sockets

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))

APP_FILE = 'app.py'
ROUTES = './database/route.txt'
SOCKETS = './database/socket.txt'
HOST = "0.0.0.0"
PORT = "5000"

# Routine Job
export_routes(APP_FILE,ROUTES)
export_sockets(APP_FILE,SOCKETS)

class Config:
    """ Base config"""
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Secrets
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')

class ProdConfig(Config):
    """ Production Config """
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    """ Development Config """
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')