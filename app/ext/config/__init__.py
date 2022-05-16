import os 

basedir = os.path.abspath(os.path.dirname(__file__))


def init_app(app):
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or "teste-development2"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "econovolt.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True   # editar o template no browser.
        app.config["DEBUG_TB_PROFILER-ENABLED"] = True