import datetime, os

SECRET_KEY = os.getenv('SECRET_KEY')
APP_MODE = os.getenv('FLASK_ENV')
DEBUG = os.getenv('DEBUG')
FLASK_APP = os.getenv('FLASK_APP')
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_DEBUG = os.getenv('MAIL_DEBUG')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

IMAGE_UPLOADS = os.getenv('IMAGE_UPLOADS')