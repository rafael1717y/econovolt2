from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required

from app.ext.auth.models import Item, Order, Order_Item, User
from app.ext.db import db

# Para proteger o admin com login
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


admin = Admin()

# TODO: Admin desativado para rodar os testes e em produção uma vez que
# até o momento exigido apenas login para acesso -> /admin/user
def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Econovolt")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.add_view(ModelView(Item, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Order_Item, db.session))
    admin.init_app(app)
