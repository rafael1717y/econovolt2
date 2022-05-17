from flask import Flask
from app.ext import config


def create_app():
    """"Factory para criar um app Flask. """
    app = Flask(__name__)
    config.init_app(app)
    #db.init_app(app)
    #auth.init_app(app)
    #admin.init_app(app) 
    #migrate.init_app(app)
    #cli.init_app(app)
    #toolbar.init_app(app)
    #site.init_app(app)
    return app
