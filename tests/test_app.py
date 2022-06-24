from flask import url_for

from app.ext.auth.models import User


# Exemplo de teste
def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250


# Teste de config. do app
def test_app_is_created(app):  # app recebido por injeção de dependência
    # Testa se o app foi criado.
    assert app.name == "app"


def test_email_admin(app):
    assert app.config["ADMINS"] == ["econovoltsimulador@gmail.com"]


def test_config_email_port(app):
    assert app.config["MAIL_PORT"] == 25


# Usando a fixture client
def test_request_returns_404(client):
    assert client.get("/url_inexistente").status_code == 404


def test_request_return_200(client):
    assert client.get("/").status_code == 200


def test_request_return_200_about(client):
    assert client.get("/about").status_code == 200


def test_password_hashing(app):
    """Verificação do senha do usuário salva"""
    u = User(username="usuario1")
    u.set_password("1234")
    assert u.check_password("4321") == False
    assert u.check_password("1234") == True


def test_avatar(app):
    u = User(username="john", email="john@example.com")
    assert u.avatar(128), (
        "https://www.gravatar.com/avatar/"
        "d4c74594d841139328695756648b6bd6"
        "?d=identicon&s=128"
    ) == True


def test_avatar_rafael_incorreto(app):
    u = User(username="rafael", email="rafaelufjf@gmail.com")
    assert u.avatar(128), (
        "https://www.gravatar.com/avatar/"
        "16b141790f08f6170fa643b0f9f7ed10"
        "?d=identicon&s=128"
    ) == False


def test_url_for_about(client):
    """Test da página de sobre."""
    assert client.get(url_for("site.about", external=True)).status_code == 200


def test_visualizacao_de_simulacao_nao_visivel_na_home(client):
    assert client.get(url_for("site.simulator", external=True)).status_code != 200


def test_url_login(client):
    assert client.get(url_for("site.login", external=True)).status_code == 200
