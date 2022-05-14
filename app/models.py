from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
import jwt
from app import app
from time import time
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    simulations = db.relationship('Simulation', backref='author', lazy='dynamic')


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode("utf-8")).hexdigest()
        return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(
            digest, size
        )

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {"reset_password": self.id, "exp": time() + expires_in},
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])[
                "reset_password"
            ]
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return "<User {}>".format(self.username)


class Simulation(db.Model):  #s = Simulation(item='geladeira', quantity=1, author=u)
     __tablename__ = 'Simulation'

     id = db.Column(db.Integer, primary_key=True)
     item = db.Column(db.String(120), index=True)
     quantity = db.Column(db.Integer)
     time_of_use = db.Column(db.Integer)
     potency = db.Column(db.Integer)
     state = db.Column(db.String(2))  # Estado ---lista escolhas // tarifa por estado ??
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     result = db.relationship('Result', backref='simulation', lazy='dynamic')


     def __init__(self, item, quantity, time_of_use, potency, state, user_id):
         self.item = item
         self.quantity = quantity
         self.time_of_use = time_of_use
         self.potency = potency
         self.state = state
         self.user_id = user_id


     def insert(self):
         db.session.add(self)
         db.session.commit()

     
     def update(self):
         db.session.commit()


     def delete(self):
         db.session.delete(self)
         db.session.commit()


     def detail(self):
         return {
             'user_id': self.user_id,
             'item': self.item,
             'quantity': self.quantity,
             'time_of_use': self.time_of_use,
             'potency': self.potency,
             'state': self.state,
        }

     def calcular_custo(self):
         print('calculando...')
         valor_total = []
         all = Simulation.query.all()
         for i in all:
             print('Id do item >>', i.id)
             print('Nome do item >>', i.item)
             # teste multiplicando apenas  potência x número de horas [tempo de uso] x quantidade
             valor_parcial = (i.potency * i.time_of_use * i.quantity)
             print('Valor parcial >>>', valor_parcial) 
             valor_total.append(valor_parcial)   
         print('Valor Total >>', sum(valor_total))
         


     def __repr__(self):
         return "Item incluído para simulação >>> {}".format(self.item)  # retorna simul. item


    
class Result(db.Model):
    __tablename__ = 'Result'
    
    id = db.Column(db.Integer, primary_key=True)
    simulation_id = db.Column(db.Integer, db.ForeignKey('Simulation.id'), nullable=False) #'simulation.id
    consumption = db.Column(db.Integer)
    tax = db.Column(db.Integer) # armazena o valor do cálculo
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)     


    def __init__(self, simulation_id, timestamp):
        self.simulation_id = simulation_id
        self.timestamp = timestamp


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def detail(self):
        return {
            "simulation_id": self.simulation_id,
            "timestamp": self.timestamp,
        }

    def exibir_custo(self):
        print('Exibir custo')
        #self.tax = (self.Simulation.quantity * self.Simulation.potency)
        #print('li 135', self.tax)
        #return f"A tarifa calculada foi {self.tax}"



    def __repr__(self):
        return "Resultado de uma simulação {}".format(self.tax)



    
# Fora da classe
# ---------------
@login.user_loader  # da classe
def load_user(id):
    return User.query.get(int(id))


#


#s = Simulation(item="geladeira", quantity=8, time_of_use=10, potency=100, state="MG", user_id=1)
#for key, values in s.detail().items():
#{'user_id': 1, 'item': 'tv', 'quantity': 8, 'time_of_use': 10, 'potency': 100, 'state': 'MG'}
#s.insert() -- db.session.commit(u)
#all = s.query.all()  [Item incluído para simulação >>> tv, Item incluído para simulação >>> geladeira]

"""
jogar tudo em all 
all = s.query.all()
for item in all:
    print(item.quantity)
    print(item.id)
"""