from turtle import title
from flask import current_app, flash, request, render_template, redirect, url_for
from flask import Blueprint
from app.ext.auth.forms import LoginForm
from app.ext.auth.models import User 
from app.ext.db import db 
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
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
@login_required
def index():
    current_app.logger.debug("Entrei na função index")
    return render_template("index.html", title="Home Page")


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
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = LoginForm()
    if form.validate_on_submit():
        print('linha 51')
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nome de usuário ou senha inválido(s).')
            print('linha 55')        
            return redirect(url_for('site.login'))
        login_user(user, remember=form.remember_me.data)  
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('site.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Entrar', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.index'))