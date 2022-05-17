from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    g,
    jsonify,
    current_app,
)
from flask_login import current_user, login_required
from app import db
from app.ext.main.forms import NewSimulationForm
from app.models import User, Simulation
from app.ext.main import bp
import pdb


""""
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():    
    return render_template("index.html")
"""


@bp.route("/new_simulation", methods=["GET", "POST"])
@login_required
def new_simulation():
    form = NewSimulationForm()
    if form.validate_on_submit():
        simulation = Simulation(
            item=form.item.data,
            quantity=form.quantity.data,
            potency=form.potency.data,
            time_of_use=form.time_of_use.data,
            state=form.state.data,
            author=current_user,
        )
        db.session.add(simulation)
        db.session.commit()
        flash("O item foi adicionado para simulação.")
        # calcularcusto()
        return redirect(url_for("main.new_simulation"))
    return render_template("teste.html", title="Simulações", form=form)


@bp.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    valor_total = []
    all = Simulation.query.all()
    for i in all:
        print("Id do item >>", i.id)
        print("Nome do item >>", i.item)
        # P/teste: multiplicando apenas  potência x número de horas [tempo de uso] x quantidade
        valor_parcial = i.potency * i.time_of_use * i.quantity
        print("Valor parcial >>>", valor_parcial)
        valor_total.append(valor_parcial)

    valor_total = sum(valor_total)
    return render_template(
        "user.html", user=user, valor_total=valor_total, simulations=all
    )


@login_required  # um usuário logado pode ver sua simulação
@bp.route("/simulations")
def simulations():
    # return render_template(url_for('simulations', title='Simulações', simulations=simulations))
    return render_template("simulations.html", title="Simulações")


# Ajax - ainda que não esteja submetendo os dados eles estão no form data.
@login_required
@bp.route("/process", methods=["POST"])
def process():
    email = request.form["email"]
    name = request.form["name"]
    print("linha 135", email)
    print("linha 136", name)
    if name and email:  ## validac e calc aqui >> simulacoes >> resultado no final
        msg = "Dados incluídos com sucesso. "
        # guardar(email)
        return jsonify({"name": name, "email": email, "msg": msg})
    return jsonify({"error": "Faltando dados!"})


# 2. Exibe o resultado das simulações após cálculo método para calcular custo na classe Simulation]
@bp.route("/display_simulations", methods=["GET", "POST"])
@login_required
def display_simulations():
    print("calculando...")
    valor_total = []
    # all = Simulation.query.all()
    all = (
        current_user.simulations.all()
    )  ##?? mostrar as simulações só do usuário atual logado
    print("linha 182>> ", all)
    for i in all:
        print("Id do item >>", i.id)
        print("Nome do item >>", i.item)
        # print("Timestamp >>", i.timestamp)
        # P/teste: multiplicando apenas  potência x número de horas [tempo de uso] x quantidade
        valor_parcial = i.potency * i.time_of_use * i.quantity
        print("Valor parcial >>>", valor_parcial)
        valor_total.append(valor_parcial)

    valor_total = sum(valor_total)
    print("Valor Total >>", valor_total)
    return render_template(
        "display_simulations.html", user=user, valor_total=valor_total, simulations=all
    )


@bp.route("/display", methods=["GET", "POST"])
@login_required
def display():
    return redirect(url_for("main.display_simulations"))


@bp.route("/total", methods=["GET", "POST"])
# @login_required
def total():
    return render_template("total.html")


@bp.route("/simulations_by_user/<string:username>")
def simulations_by_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    simulations = current_user.simulations.all()
    return render_template(
        "user.html",
        user=user,
        simulations=simulations,
    )
