from ensurepip import bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config



app = Flask(__name__)
app.config.from_object(Config)



# Registro das extensões
# -----------------------
bootstrap = bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


# Depois da instância da aplicação criada: 
# ----------------------------------------
from app import routes, models, errors