from flask import Flask, request, redirect, url_for, render_template, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'test-development'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
Bootstrap(app)


@login_manager.user_loader
def current_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    __tablename = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
   
    def __str__(self):
        return self.name






@app.route("/")  # users
def index():
    users = Users.query.all()   # select * from users;
    return render_template("users.html", users=users)


@app.route("/user/<int:id>")  # user
@login_required                 ### TODO
def unique(id):
    user = Users.query.get(id)
    return render_template("user.html", user=user)




# Deletar um usuário -- simulações depois
@app.route("/user/delete/<int:id>")
def delete(id):
    user = Users.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/")


@app.route('/redirect')
def redirect2():
    return redirect(url_for("response"))


@app.route('/response')
def response():
    return render_template("response.html")


@app.route("/users")
@app.route("/users/<int:id>")
#@login_required     # somente usuários logados podem ver simulações
def users(id):
    titulo = request.args.get("titulo")
    user = dict(
        path = request.path, 
        referrer=request.referrer, 
        content_type=request.content_type, 
        method=request.method,
        titulo = titulo, 
        id = id if id else 0
    )
    return render_template("users.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users()
        user.name = request.form["name"]
        user.email = request.form["email"]
        user.password = generate_password_hash(request.form["password"])
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso!")
        return redirect(url_for("index"))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = Users.query.filter_by(email=email).first()
        #errors = {}

        if not user:
            flash('Email inválido.')
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash("Credencias inválidas.")
            return redirect(url_for("login"))
        
        login_user(user)
        return redirect(url_for("simulator"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("users.html")

# TODO: enviar resultados simulações calculados em uma rota para o template


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/simulator')  # se logado vai pra página de simulação
@login_required
def simulator():
    flash("Bem-vindo ao simulador!!!!!")
    return render_template("simulator.html")


# ------------------------
if __name__ == "__main__":
    app.run()