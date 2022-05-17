from flask import Flask
from app.ext import site
from app.ext import toolbar
from app.ext import config
from app.ext import db
from app.ext import migrate
from app.ext import cli
from app.ext import auth
from app.ext import admin


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)  # iniciar flask admin depois da autenticação
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
