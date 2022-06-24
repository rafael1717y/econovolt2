import pytest
from flask import Flask

from app.ext import config


# Fixture criação do app
@pytest.fixture(scope="module")
def app():
    """Instância de uma aplicação Flask..."""
    app = Flask(__name__)
    config.init_app(app)
    from app import create_app

    return create_app()


# Exemplos de fixtures pytest
@pytest.fixture
def define_target():
    return {"url": "smtp.gmail.com", "port": 587}


@pytest.fixture
def smtp_connection(define_target):
    import smtplib

    url = define_target["url"]
    port = define_target["port"]
    return smtplib.SMTP(url, port, timeout=5)
