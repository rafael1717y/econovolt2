from flask import request 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired



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
