from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.ext.auth.models import User # importe da classe User de models da extensão de autenticação


class LoginForm(FlaskForm):
    "Criação do formulário de login. "
    username = StringField("Nome", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Lembrar-me")
    submit = SubmitField("Entrar")



