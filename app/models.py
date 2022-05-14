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
     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     


     # TODO: Ajustar modelos de dados e vincular as simulações a um único id [user_id]
     # TODO: Como um post vinculado a um unico usuário.
     # TODO: Estudo livro Grinberg -- um usuário um post [relação]
     
    
     def mostrar_simulacoes_usuario(self):
         pass

     def __repr__(self):
         return f"{self.item} de id: {self.id} incluído na simulação para o usuário de id {self.user_id}"


     def calcular_tarifa_uma_simulacao(self): #queries aqui
         pass


     def calcular_total_simulado(self):
         pass
             


    
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

# Aqui = s = Simulation(item='geladeira', quantity=10, time_of_use=1, potency=10, state='MG', author=u)
#simulations = u.simulations.all()
#s = Simulation.query.all()
#for s in s:
#...   print(s.id, s.author.username, s.item)


# AQUI
# ------------------------------------------------
#obter a simulação de um usuário
##simulacao_usuario_1 = u.simulations.all()
# simulacao_usuario_2 = u2.simulations.all()
#>>> simulacao_usuario_2
#[geladeira de id: 2 incluído na simulação para o usuário de id 2]

"""
totals = Simulation.query.all()
lista = []
for s in totals:
    lista.append(s.quantity)
sum(lista)

totals =Simulation.query.all()
for s in totls:
    print(s.timestamp)
"""



"""
tudo em all 
all = s.query.all()
for item in all:
    print(item.quantity)
    print(item.id)
"""