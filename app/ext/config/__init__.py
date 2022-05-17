import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dynaconf import FlaskDynaconf


def init_app(app):
    # TODO: para settings.toml
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "econovolt.db")
    
    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")