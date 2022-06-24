import pytest

from app import create_app

app = create_app()

@pytest.fixture(scope="module")
def app():
    """Instância de uma aplicação flask....."""
    app.config["SECRET_KEY"] = "hahah"
    return create_app()
