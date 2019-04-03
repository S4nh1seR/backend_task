import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strong-password'
    SECURITY_PASSWORD_SALT = 'password-salt'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    MAIL_USERNAME = 'sanhiserrrr@gmail.com'
    MAIL_PASSWORD = 'clxl aixm ozur kllm'
    # MAIL_DEFAULT_SENDER = 'SanhiseR@mail.ru'
    # MAIL_DEFAULT_SENDER = 'ryaschikov.ap@phystech.edu'
