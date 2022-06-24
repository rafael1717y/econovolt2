from flask_wtf import FlaskForm
from wtforms import (HiddenField, IntegerField, SelectField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired


class AddItem(FlaskForm):
    name = StringField("Nome")
    total_days_of_use_in_month = IntegerField("Dias de uso em um mês")
    average_daily_use_hours = IntegerField("Média de uso diário em horas")
    average_daily_use_minutes = IntegerField("Média de uso diário em minutos")
    average_power = IntegerField("Potência média")
    description = TextAreaField("Descrição")
    # colocar imagens dos itens ?


class AddToSimulator(FlaskForm):
    quantity = IntegerField("Quantity")
    id = HiddenField("ID")


class InfoUserForm(FlaskForm):
    dealership = SelectField(
        "Concessionária de Energia:",
        choices=["Cemig", "Eletropaulo"],
        option_widget=None,
        validate_choice=True,
    )
    energy_bill = IntegerField(
        "Valor da sua última conta de energia:", validators=[DataRequired()]
    )
    submit = SubmitField(label=("Confirmar"))


class NewSimulationForm(FlaskForm):
    dealership = SelectField(
        "Concessionária de Energia:",
        choices=["Cemig", "Eletropaulo"],
        option_widget=None,
        validate_choice=True,
    )
    state = SelectField(
        "Estado:",
        choices=["MG", "SP", "RJ", "BA", "RS", "AC"],
        option_widget=None,
        validate_choice=True,
    )
    energy_bill = IntegerField(
        "Valor da sua última conta de energia:", validators=[DataRequired()]
    )
    item = SelectField(
        "Item:",
        choices=["Geladeira", "Umidificador", "Chuveiro", "TV", "Ar-Condicionado"],
        option_widget=None,
        validate_choice=True,
    )
    item_quantity = IntegerField("Quantidade:", validators=[DataRequired()])
    hours_of_daily_use = IntegerField(
        "Tempo de uso em horas:",
        validators=[DataRequired()],
    )
    potency = IntegerField("Potência em W:", validators=[DataRequired()])
    submit = SubmitField(label=("Adicionar"))


# " ""Comparar valor de entrada da conta com o obtido na simulação"""
class Checkout(FlaskForm):
    name = StringField("nome da simulação")
    state = SelectField(
        "Estado",
        choices=["MG", "SP", "RJ", "BA", "RS", "AC"],
        option_widget=None,
        validate_choice=True,
    )
    dealership = SelectField(
        "Concessionária de Energia:",
        choices=["Cemig", "Energisa", "Eletropaulo"],
        option_widget=None,
        validate_choice=True,
    )
