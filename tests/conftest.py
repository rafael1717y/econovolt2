import pytest
from app import create_app

# Fixtures
@pytest.fixture
def define_target():
    return {'url': 'smtp.gmail.com', 'port': 587}

@pytest.fixture
def smtp_connection(define_target):
    import smtplib
    url = define_target['url']
    port = define_target['port']    
    return smtplib.SMTP(url, port, timeout=5)
    

"""
@pytest.fixture(scope="module")
def app():
    # Instância de uma aplicação flask.....
    #return create_app()
"""
