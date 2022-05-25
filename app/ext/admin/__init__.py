from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from app.ext.db import db
#from app.ext.db.models import Dealership, Simulation, Items, Order, OrderItems, Result




from flask_admin.base import AdminIndexView
from flask_login import login_required


# Para proteger o admin com login
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)



admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Econovolt")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)
    
    # Adicionar o model de Resultados
    # TODO: Traduzir para pt-br.
