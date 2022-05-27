from typing import Text
from flask import request 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, HiddenField
from wtforms.validators import ValidationError, DataRequired



class AddItem(FlaskForm):
    name = StringField("Nome")
    total_days_of_use_in_month = IntegerField("Dias de uso em um mês")
    average_daily_use = IntegerField("Média de uso diário")
    average_power  = IntegerField("Potência média")
    description = TextAreaField("Descrição")
    # colocar imagens dos itens ?



class AddToSimulator(FlaskForm):
    quantity = IntegerField('Quantity')
    id = HiddenField('ID')


# TODO: separ
class InfoUserForm(FlaskForm):
    dealership = SelectField("Concessionária de Energia:", choices=["Cemig", "Eletropaulo"], option_widget=None, validate_choice=True) 
    energy_bill = IntegerField("Valor da sua última conta de energia:",  validators=[DataRequired()])
    submit = SubmitField(label=('Confirmar'))



class NewSimulationForm(FlaskForm):
    dealership = SelectField("Concessionária de Energia:", choices=["Cemig", "Eletropaulo"], option_widget=None, validate_choice=True) 
    state = SelectField("Estado:", choices=["MG", "SP", "RJ"], option_widget=None, validate_choice=True)
    energy_bill = IntegerField("Valor da sua última conta de energia:",  validators=[DataRequired()])
    item = SelectField("Item:", choices=["Geladeira", "Umidificador", "Chuveiro", "TV", "Ar-Condicionado"], option_widget=None, validate_choice=True)
    item_quantity = IntegerField("Quantidade:", validators=[DataRequired()]) 
    hours_of_daily_use  = IntegerField("Tempo de uso em horas:", validators=[DataRequired()], ) 
    potency = IntegerField("Potência em W:", validators=[DataRequired()])
    submit = SubmitField(label=('Adicionar'))



class Checkout(FlaskForm):
    name = StringField("Nome")
    state = SelectField("Estado", choices=["MG", "SP", "RJ"], option_widget=None, validate_choice=True)
    dealership = SelectField("Concessionária de Energia:", choices=["Cemig", "Eletropaulo"], option_widget=None, validate_choice=True) 






