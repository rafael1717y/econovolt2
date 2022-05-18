from flask import current_app, flash, request, render_template, redirect, url_for
from flask import Blueprint
from app.ext.auth.forms import LoginForm
from app.ext.auth.models import User 
from app.ext.db import db 
import pdb

"""
1. Criação de um blueprint em main [nome + path import.] para componentização
2. Registro do blueprint em __init__.py dentro da pasta site.
3. Criação das rotas do blueprint.
4. Chamada do bp em create_app.
5. flask routes ou usar DebugToolbar para ver as rotas.
6. pdb.set_trace() para analisar o request. 
"""


bp = Blueprint("site", __name__)


# Registro das rotas principais
# ------------------------------
@bp.route("/")
@bp.route('/index')
def index():
    current_app.logger.debug("Entrei na função index")
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/simulations")
def simulations():
    return render_template("simulations.html")


# Rotas de autenticação
# -------------------------------------------------
# 2. Dentro do blueprint cria-se a rota para o form.
@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login solicitado pelo usuário {}, lembrar-me={}".format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('site.index'))
    return render_template('auth/login.html', title='Entrar', form=form)



