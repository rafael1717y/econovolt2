from datetime import datetime
from time import time
import datetime
from app.ext.db import db


class Simulation(db.Model):
    __tablename__ = "Simulation"

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(120), index=True)
    quantity = db.Column(db.Integer)
    time_of_use = db.Column(db.Integer)
    potency = db.Column(db.Integer)
    state = db.Column(db.String(2))
    publish_date = db.Column(db.DateTime(), index=True, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    on_menu = db.Column(db.Boolean)  # decidir se aparecerá ou não no menu.
