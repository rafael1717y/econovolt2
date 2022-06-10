from email.errors import FirstHeaderLineIsContinuationDefect

from flask import Markup, flash
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters

from app.ext.auth.models import User
from app.ext.db import db

# from flask_admin.contrib.mongoengine


def format_user(self, request, user, *args):
    """Customiza o campo 'user' para retornar
    apenas o nome do email.Obs.: Self representa a
    própria instância do admin nesse caso."""
    return user.email.split("@")[0]  # só o nome


class UserAdmin(ModelView):
    """Interface administrativa de usuários."""

    # formatação de uma coluna
    # column_formatters = {"email": format_user}
    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }
    # lambda s, r, u, *a: Markup(f'<b>(u.email.split("a")[0]}</b>')
    # escolha das colunas que serão exibidas.
    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email, "dominio", options=(("gmail", "Gmail"), ("uol", "Uol"))
        ),
    ]

    # customização do perfil
    can_edit = False
    can_create = True
    can_delete = True

    @action("toggle_admin", "Toggle admin status", "Are you sure?")
    def toggle_admin_status(self, ids):
        """Mudar o status de admin para usuário"""
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            # select pra trazer os usuários com id selecionados
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} usuários alterados com sucesso!", "success")

    @action("send email", "Send email to all users", "Are you sure?")
    def send_email(self, ids):
        """Enviar email."""
        users = User.query.filter(User.id.in_(ids)).all()
        # TODO: 1) redirect para um form para escrever a mensagem do email.
        #       2) enviar o email
        for user in users:
            pass
            # select pra trazer os usuários com id selecionados
            # enviar email
            # db.session.commit()
        flash(f"{len(users)} um email enviado", "success")
