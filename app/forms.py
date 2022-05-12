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
        item_1 = SelectField("Itens", choices=["Geladeira", "Umidificador", "Chuveiro"], option_widget=None, validate_choice=True)
        quantidade_1 = SelectField("Quantidade", choices=["1", "2", "3", "4", "5"], option_widget=None, validate_choice=True)
        tempo_de_uso_1 = IntegerField("Tempo de uso em minutos")
        potencia_1= IntegerField("Potência")

        item_2 = SelectField("Itens", choices=["Geladeira", "Umidificador", "Chuveiro"], option_widget=None, validate_choice=True)
        quantidade_2 = SelectField("Quantidade", choices=["1", "2", "3", "4", "5"], option_widget=None, validate_choice=True)
        tempo_de_uso_2 = IntegerField("Tempo de uso em minutos")  # ou horas
        potencia_2= IntegerField("Potência")



        submit = SubmitField("Adicionar")
