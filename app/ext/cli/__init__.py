import click

from app.ext.db import models  # noqa
from app.ext.db import db


def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db. Usar flask --help para ver comandos
        disponíveis. Ex.: fora do shell flask create-db"""
        try:
            db.create_all()
        except:
            print("Não foi possível criar o db.")

    @app.cli.command()
    def list_simulations():
        click.echo("lista de simulações")
