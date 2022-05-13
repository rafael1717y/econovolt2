from app import app, db
from app.models import User, Simulation


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, 'Simulation': Simulation}
