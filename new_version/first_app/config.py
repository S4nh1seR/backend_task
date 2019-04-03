import os
basedir = os.path.abspath(os.path.dirname(__file__))

#POSTGRES_URL = "database:5432"
#POSTGRES_USER = "postgres"
#POSTGRES_PW = "example"
#POSTGRES_DB = "postgres"

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'strong-password'
    SECURITY_PASSWORD_SALT = 'password-salt'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/#{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
