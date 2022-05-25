from email.mime import image
from unicodedata import name
from flask import current_app, flash, jsonify, request, render_template, redirect, url_for, escape
from flask import Blueprint
from app import email
from app.ext.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.ext.main.forms import AddItem, NewSimulationForm, InfoUserForm
from app.ext.auth.models import Item, User 
from app.ext.db import db 
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse
from app.email import send_password_reset_email
import pdb

from flask_uploads import UploadSet, configure_uploads, IMAGES
photos = UploadSet('photos', IMAGES)


"""
1. Criação de um blueprint em main [nome + path import.] para componentização
2. Registro do blueprint em __init__.py dentro da pasta site.
3. Criação das rotas do blueprint.
4. Chamada do bp em create_app.
5. flask routes ou usar DebugToolbar para ver as rotas.
6. pdb.set_trace() para analisar o request. 
"""


bp = Blueprint("site", __name__)


# 01. Registro das rotas principais
# ------------------------------
@bp.route("/")
@bp.route('/index')
def index():
    log_request(request, request.data)
    return render_template("index.html", title="Home Page")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/simulations")
def simulations():
    return render_template("simulations.html")


# Rotas de autenticação e registro de usuários
# 2. Dentro do blueprint cria-se a rota para o form.
# --------------------------------------------------
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


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("site.index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Você agora está cadastrado!")
        return redirect(url_for("site.login"))
    return render_template("auth/register.html", title="Cadastrar", form=form)


# 03. Rotar para tratamento de erros
# --------------------------------------
# TODO: Blueprint de erros.

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500



# 04. Rotas email
@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print('linha 115 - user >', user)
        if user:
            send_password_reset_email(user)
        flash("As instruções para criação de uma nova senha foram enviadas para o seu email.")
        return redirect(url_for('site.login'))
    return render_template('auth/reset_password_request.html', title='Nova senha', form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('site.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('site.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Sua senha foi alterada.")
        return redirect(url_for('site.login'))
    return render_template('auth/reset_password.html', form=form)





# 05. Rotas das simulações
# ---------------------------
@bp.route('/user/<username>')
#@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    simulations = [
        {'author': user, 'item': 'resultado #1'},
        {'author': user, 'item': 'resultado #2'},
    ]
    return render_template('user.html', user=user, simulations=simulations)


#Logs 

def log_request(req, res):
    with open('econovoltt.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@bp.route('/view_logs')
@login_required
def view_the_log():
    contents = []
    with open('econovoltt.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='Logs', the_row_titles=titles, the_data=contents, )




# -----------------------------------------------
# PAREI AQUI
@bp.route('/new_simulation', methods=['GET', 'POST'])
#@login_required
def new_simulation():  ### mostra os itens disponíveis para escolha [homepage?]
    print('linha 160')  
    items = Item.query.all()
    return render_template('new_simulation.html', items=items)
# -------------------------------------------------------------
    

# Exibe informações detalhadas de um item
@bp.route('/item/<id>', methods=['GET', 'POST'])
def item(id):
    return render_template('view_item.html')




# Rotas admin

@bp.route('/admin2')
def admin():
    print('linha 202')
    items = Item.query.all()
    print('Primeiro item do db >>', items[0].name)
    return render_template('admin/index.html', admin=True, items=items)



@bp.route('/admin2/add', methods=["GET", "POST"])
def add():
    form = AddItem()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.total_days_of_use_in_month.data)
        print(form.average_daily_use.data)
        print(form.average_power.data)
        print(form.description.data)
        print(form.image.data)

        image_url = photos.url(photos.save(form.image.data))
        print('linha 218>> image_url', image_url)


        ## observar esta com itens [unique]
        new_item = Item(name=form.name.data, total_days_of_use_in_month=form.total_days_of_use_in_month.data,
          average_daily_use=form.average_daily_use.data, average_power=form.average_power.data, 
          description=form.description.data, image=image_url)

        db.session.add(new_item)
        db.session.commit()
        print('linha 255')
        
        return redirect(url_for('site.admin'))
    
    return render_template('admin/add-item.html', admin=True, form=form)



@bp.route('/admin2/view_simulation')  #order
def order():
    return render_template('admin/view-simulation.html', admin=True)






#
