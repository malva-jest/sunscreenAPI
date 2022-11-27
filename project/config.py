from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

