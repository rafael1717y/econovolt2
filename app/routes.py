import json
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app.forms import ResetPasswordRequestForm, ResetPasswordForm, NewSimulationForm
from app.email import send_password_reset_email
import pdb

@app.route("/")  # users
def index():
    # users = Users.query.all()   # select * from users;
    # return render_template("users.html", users=users)
    return render_template("index.html")


@login_required  # um usuário logado pode ver sua simulação
@app.route("/simulations")
def simulations():
    # return render_template(url_for('simulations', title='Simulações', simulations=simulations))
    return render_template("simulations.html", title="Simulações")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Nome de usuário ou senha inválido(s)")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return render_template("simulations.html")  # TODO usar url_for
    return render_template("login.html", title="Entrar", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Você agora está cadastrado!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Cadastrar", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    simulations = [
        {"author": user, "body": "Simulação #1"},
        {"author": user, "body": "Simulação #2"},
    ]
    return render_template("user.html", user=user, simulations=simulations)


@app.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(
            "As instruções para a criação de uma nova senha foram enviadas para o seu email."
        )
        return redirect(url_for("login"))
    return render_template(
        "reset_password_request.html", title="Criar nova senha", form=form
    )


@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash("Sua senha foi alterada.")
        return redirect(url_for("login"))
    return render_template("reset_password.html", form=form)


# View para realizar uma simulação
"""
@app.route("/new_simulation", methods=["GET", "POST"])
def new_simulation():
    #pdb.set_trace()
    form = NewSimulationForm()
    if request.method == "POST":
        print(form.item.data,
              form.quantidade.data)
        return redirect(url_for("index"))
    return render_template("new_simulation.html", form=form)
"""
# 
@app.route("/new_simulation", methods=["GET", "POST"])
def new_simulation():
    return render_template('new_simulation.html')


simulations = []
def guardar(email):
    simulations.append(email)
    print('134', simulations)


# Ainda que não esteja submetendo os dados eles estão no form data. 
@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    print('linha 135', email)
    print('linha 136', name)
    if (name and email):  ## validac e calc aqui >> simulacoes >> resultado no final
        msg = 'Dados incluídos com sucesso. '
        guardar(email)
        return jsonify({'name': name, 'email': email, 'msg': msg})
    return jsonify({'error': 'Faltando dados!'})


