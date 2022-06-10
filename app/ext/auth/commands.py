import click

from app.ext.auth.models import User
from app.ext.db import db


@click.option("--username", "-u")
@click.option("--email", "-e")
@click.option("--password_hash", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(username, email, password_hash, admin):
    "Adiciona um novo usuário."
    # TODO: tratar erros - Operation error?
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        admin=admin,
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"Usuário {email} criado com sucesso!")


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuários {users}")
