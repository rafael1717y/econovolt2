from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.ext.db import db
from app.ext.db.models import Simulation


admin = Admin()


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Econovolt")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)
    admin.add_view(
        ModelView(Simulation, db.session)
    )  # se nao quer especializar uma classe pode-se usar o ModelView direto.
    # Adicionar o model de Resultados
    # TODO: Traduzir para pt-br.
