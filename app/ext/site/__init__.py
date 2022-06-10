from .main import \
    bp  # 1. importação do blueprint do arquivo site da pasta main


def init_app(app):
    app.register_blueprint(
        bp
    )  # 2. registro do blueprint = app.register_blueprint(bp) em __init__.py
