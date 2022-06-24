from app.ext.auth.models import User


def test_app_is_created(app):  # app recebido por injeção de dependência
    """Testa se o app foi criado."""
    assert app.name == "app"


def test_email_admin(app):
    assert app.config["ADMINS"] == ["econovoltsimulador@gmail.com"]


# Usando a fixture client
def test_request_returns_404(client):
    assert client.get("/url_inexistente").status_code == 404


def test_request_return_200(client):
    assert client.get("/").status_code == 200


def test_password_hashing(app):
    u = User(username="susan55")
    u.set_password("senha123")
    assert u.check_password("senha123") == True
    assert u.check_password("senha124") == False
