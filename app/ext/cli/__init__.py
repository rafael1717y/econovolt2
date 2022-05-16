import click
from app.ext.db import db 
from app.ext.db import models 



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
    @click.option("--username", "-u")
    @click.option("--email", "-e")
    @click.option("--password_hash", "-p")
    @click.option("--admin", "-a",is_flag=True, default=False)
    def add_user(username, email, password_hash, admin):
        "Adiciona um novo usuário."
        # TODO: tratar erros - Operation error?
        user = models.User(
            username=username, 
            email = email,
            password_hash=password_hash,
            admin=admin, 
        )
        db.session.add(user)
        db.session.commit()  

        click.echo(f"Usuário {email} criado com sucesso!")


    @app.cli.command()
    def list_simulations():
        # TODO: usar a biblioteca tabulate
        click.echo('lista de simulações')


    @app.cli.command()
    def list_users():
        click.echo('lista de usuários')



    #TODO comando para criar uma simulação