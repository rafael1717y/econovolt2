from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, RadioField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

"""
Criação dos formulários de login, solicitação de nova senha, alteração e 
registro de um usuário.
"""


class LoginForm(FlaskForm):
    username = StringField("Nome", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    remember_me = BooleanField("Lembrar-me")
    submit = SubmitField("Entrar")


class ResetPasswordRequestForm(FlaskForm):
    email = StringField("Informe seu email:", validators=[DataRequired(), Email()])
    submit = SubmitField("Solicitar nova senha")


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Senha", validators=[DataRequired()])
    password2 = PasswordField(
        "Repita a senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Confirmar")


class RegistrationForm(FlaskForm):
    username = StringField("Nome", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    password2 = PasswordField(
        "Repita a senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Cadastrar")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Por favor, use um nome diferente.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Por favor, use um email diferente.")


class NewSimulationForm(FlaskForm):
        # as categorias deverão vir do db?? Colocar apenas itens maior consumo??
        # Para um item -- ou um for com o num itens??
        item = SelectField("Item:", choices=["Geladeira", "Umidificador", "Chuveiro", "TV", "Ar-Condicionado"], option_widget=None, validate_choice=True)
        quantity = IntegerField("Quantidade:", validators=[DataRequired()]) 
        time_of_use = IntegerField("Tempo de uso em horas:", validators=[DataRequired()], ) 
        potency = IntegerField("Potência em W:", validators=[DataRequired()])
        state = SelectField("Estado:", choices=["MG", "SP", "RJ"], option_widget=None, validate_choice=True)
        submit = SubmitField(label=('Adicionar'))
        
