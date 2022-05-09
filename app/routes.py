from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route("/")  # users
def index():
    #users = Users.query.all()   # select * from users;
    #return render_template("users.html", users=users)
    return render_template("base.html")


@login_required  # um usuário logado pode ver sua simulação
@app.route('/simulations')
def simulations():
    # return render_template(url_for('simulations', title='Simulações', simulations=simulations))
    return render_template('simulations.html', title='Simulações')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nome de usuário ou senha inválido(s)')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return render_template('simulations.html')   # TODO usar url_for
    return render_template('login.html', title='Entrar', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Você agora está cadastrado!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Cadastrar', form=form)



@app.route("/about")
def about():
    return render_template("about.html")




# TODO: enviar resultados simulações calculados em uma rota para o template


