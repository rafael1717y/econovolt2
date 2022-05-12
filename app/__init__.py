from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)


# Registro das extensões
# -----------------------
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
login = LoginManager(app)
login.login_view = "login"


# Boilerplate de Logs
# -------------------
# TODO: transformação em uma função
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
    app.logger.info("A aplicação Econovolt iniciou...")


# Depois da instância da aplicação criada:
# ----------------------------------------
from app import routes, models, errors
