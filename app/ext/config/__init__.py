import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dynaconf import FlaskDynaconf


def init_app(app):
    # TODO: para settings.toml
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "econovolt.db")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = os.environ.get('ADMINS')
    
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER-ENABLED = true"] = True
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS = false"] = True

    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")