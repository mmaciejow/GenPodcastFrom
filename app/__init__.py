import os

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .Config import Config

db = None

def create_app():
    global db

    # Create and configure an instance of the Flask application
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.urandom(20)

    # init and create database
    db = SQLAlchemy(app)
    from .models.YouTube import Channel, Video
    db.create_all()

    # init routes
    from .routes import routes
    app.register_blueprint(routes)

    # Logging
    if Config.ENABLE_LOGGING:
        handler = RotatingFileHandler(Config.LOG_URI, maxBytes=10000, backupCount=1)
        logging.getLogger('werkzeug').setLevel(logging.DEBUG)
        logging.getLogger('werkzeug').addHandler(handler)
        app.logger.setLevel(logging.WARNING)
        app.logger.addHandler(handler)

    return app
