import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    #SECRET_KEY = os.urandom(20)

    # Config Database
    DATABASE_NAME = 'app.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DATABASE_NAME )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Access to site
    LIMIT_ACCESS = True
    WHITE_LIST_IPS = ['127.0.0.1', '192.168.1.2', ]

    # Logging
    ENABLE_LOGGING = False
    lOG_FILE_NAME = 'app.log'
    LOG_URI = os.path.join(basedir, lOG_FILE_NAME )

