import os

basedir = os.path.abspath(os.path.dirname(__file__))

from dynaconf import FlaskDynaconf


def init_app(app):
    # Vars config na nuvem. Ex.: # sqlite em dev e postgres em prod # string de con. em
    # -> env key [DATABASE_URL] em digital ocean
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "econovolt.db")
    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
    app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT") or 25)
    app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS") is not None
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["ADMINS"] = ["econovoltsimulador@gmail.com"]    
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER-ENABLED = true"] = True
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS = false"] = True

    FlaskDynaconf(app)
    app.config.load_extensions("EXTENSIONS")
    
