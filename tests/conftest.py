import pytest

from app import create_app

app = create_app()

@pytest.fixture(scope="module")
def app():
    """Instância de uma aplicação flask....."""
    return create_app()
