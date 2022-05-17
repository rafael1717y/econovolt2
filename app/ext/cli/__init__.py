import click
from app.ext.db import db 
from app.ext.db import models  # noqa



def init_app(app):    
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db. Usar flask --help para ver comandos 
        disponíveis. Ex.: fora do shell flask create-db"""
        try:
            db.create_all()
        except:
            print('Não foi possível criar o db.')


    


    @app.cli.command()
    def list_simulations():
        # TODO: usar a biblioteca tabulate
        click.echo('lista de simulações')


   


    #TODO comando para criar uma simulação