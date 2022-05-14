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
     id = db.Column(db.Integer, primary_key=True)
     item = db.Column(db.String(120), index=True)
     quantity = db.Column(db.Integer)
     time_of_use = db.Column(db.Integer)
     potency = db.Column(db.Integer)
     state = db.Column(db.String(2))  # Estado ---lista escolhas // tarifa por estado
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     result = db.relationship('Result', backref='simulation', lazy='dynamic')

     def __repr__(self):
         return "Item incluído para simulação >>> {}".format(self.item)  # retorna simul. item


    
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumption = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)     
    simulation_id = db.Column(db.Integer, db.ForeignKey('simulation.id'))
    

    def calcular_custo(self):
        print('Calculando custo')

    def __repr__(self):
        return "Resultado de uma simulação {}".format(self.tax)



    
# Fora da classe
# ---------------
@login.user_loader  # da classe
def load_user(id):
    return User.query.get(int(id))
