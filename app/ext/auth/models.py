from flask_login import UserMixin
from datetime import datetime
from time import time
from hashlib import md5
import datetime
from app.ext.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.ext.main import login
from hashlib import md5
import jwt 
from flask import current_app, url_for


# TODO: Modelar banco de dados no vertabelo
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean)
    simulations = db.relationship("Simulation", backref="author", lazy="dynamic")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def avatar(self, size):
        """Obtém a foto do usuário no gravatar caso cadastrado ou apresenta um
        ícone padrão."""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


    def get_reset_password_token(self, expires_in=600):
        print('linha 41 - get_reset_password_token')
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256')  # TODO
        

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


    def __repr__(self):
        return "<User {}>".format(self.username)


# Fora da classe
# ---------------
@login.user_loader  # da classe
def load_user(id):
    return User.query.get(int(id))

