from flask_login import LoginManager

login = LoginManager()
login.login_view = "site.login"


def init_app(app):
    login.init_app(app)
