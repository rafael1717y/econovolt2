from audioop import add
from app.ext.auth import models 
from app.ext.auth.commands import list_users, add_user

from app.ext.db import db
from app.ext.admin import admin as main_admin
from app.ext.auth.admin import UserAdmin
from app.ext.auth.models import User



def init_app(app):
    """TODO: inicializar Flask simple login + JWT """
    app.cli.command()(list_users)  # usando o decorator como uma função que recebe outra função.
    app.cli.command()(add_user)
    main_admin.add_view(UserAdmin(User, db.session))