import re
from flask import current_app, request, render_template
from flask import Blueprint

"""
1. Criação de um blueprint em main [nome + path import.] para componentização
2. Registro do blueprint em __init__.py dentro da pasta site.
3. Criação das rotas do blueprint.
4. Chamada do bp em create_app.
"""
bp = Blueprint("site", __name__)


# Registro das rotas
# ------------------
@bp.route("/")
def index():
    current_app.logger.debug("Entrei na função index")
    return render_template("index.html")


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/simulations")
def simulations():
    return render_template("simulations.html")
