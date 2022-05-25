import datetime
from time import time
import datetime
from app.ext.db import db


class Dealership(db.Model):
    """Classe da concessionária de energia elétrica."""
    __tablename__ = 'dealership'
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    on_menu = db.Column("on_menu", db.Boolean)
    energy_bill = db.Column('energy bill', db.Numeric)

    def __repr__(self):
        return f"{self.name}"


class Simulation(db.Model): # em uma loja (store -> items, simulation -> items)
    __tablename__ = "simulation"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    dealership_id = db.Column("dealership_id", db.Integer, db.ForeignKey("dealership.id"))
    active = db.Column("active", db.Boolean)
    user = db.relationship("User", foreign_keys=user_id)
    dealership = db.relationship("Dealership", foreign_keys=dealership_id)


    def __repr__(self) -> str:
        return f"Simulacao nome: {self.name} da concessionária {self.dealership} do usuário {self.user}"
    


class Items(db.Model):
    "Classe para criação de um item"
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))     
    dealership_id = db.Column('dealership_id', db.Integer, db.ForeignKey('dealership.id'))
    dealership = db.relationship("Dealership", foreign_keys=dealership_id)
    item_quantity = db.Column('item_quantity', db.Integer) # quantidade do item
    hours_of_daily_use = db.Column('hours_of_daily_use', db.Integer)  # horas de uso diário
    potency = db.Column('potency', db.Integer)  # potência elétrica em W
    


    def __repr__(self):
        return f"Item {self.name}, quantidade {self.item_quantity}, horas {self.hours_of_daily_use} e potência {self.potency}"


    def calcular_gasto(self):
        pass


class Order(db.Model):
    __tablename__ = "order"  # para cálculo simulaçao
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    dealership_id = db.Column("dealership_id", db.Integer, db.ForeignKey("dealership.id"))
    user = db.relationship("User", foreign_keys=user_id)
    dealership = db.relationship("Dealership", foreign_keys=dealership_id)
    

    def __repr__(self):
        return f"Cálculo solicitado em {self.created_at} pelo usuário {self.user}"



class OrderItems(db.Model):
    __tablename__ = "order_items"
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    quant = db.Column("quant", db.Integer)
    id = db.Column("id", db.Integer, primary_key=True)
    order = db.relationship("Order", foreign_keys=order_id)
    items = db.relationship("Items", foreign_keys=items_id)


    def __repr__(self):
        return f"Ordem {self.order} para os items {self.items}"



class Result(db.Model): # checkout
    __tablename__ = "result"
    id = db.Column("id", db.Integer, primary_key=True)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    order = db.relationship("Order", foreign_keys=order_id)

    def __repr__(self):
        return f"Total da simulação {self.total}"

    