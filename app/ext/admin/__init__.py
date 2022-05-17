from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.ext.db import db
from app.ext.db.models import Simulation


admin = Admin()


def init_app(app):
    admin.name = "Econovolt"
    admin.template_mode = "bootstrap2"
    admin.init_app(app)
    admin.add_view(
        ModelView(Simulation, db.session)
    )  # se nao quer especializar uma classe pode-se usar o ModelView direto.
    # Adicionar o model de Resultados
    # TODO: Traduzir para pt-br.
