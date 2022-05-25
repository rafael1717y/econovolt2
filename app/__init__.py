from flask import Flask
from app.ext import config
import os
import logging
from logging.handlers import RotatingFileHandler


"""Criação do app. As extensões, exceto config, 
são carregadas pelo Dynaconf (arquivo settings.toml)
conforme o módulo (desenvolvimento ou produção)."""

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
    # Boilerplate de Logs
    # -------------------
    if not app.debug:
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/econovolt.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                '%(asctime)s  %(name)s  %(levelname)s'
                'l:%(lineno)d f:%(filename)s: %(message)s'
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info(">>> A aplicação iniciou...")

    
    return app
