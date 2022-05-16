from flask_login import UserMixin
from datetime import datetime
from time import time 
from hashlib import md5
import datetime
from app.ext.db import db

 

# TODO: Modelar banco de dados no vertabelo

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean)
    simulations = db.relationship('Simulation', backref='author', lazy='dynamic')

   
    def __repr__(self):
        return "<User {}>".format(self.username)



class Simulation(db.Model): 
     __tablename__ = 'Simulation'

     id = db.Column(db.Integer, primary_key=True)
     item = db.Column(db.String(120), index=True)
     quantity = db.Column(db.Integer)
     time_of_use = db.Column(db.Integer)
     potency = db.Column(db.Integer)
     state = db.Column(db.String(2))  
     publish_date = db.Column(db.DateTime(), index=True, default=datetime.datetime.now)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     