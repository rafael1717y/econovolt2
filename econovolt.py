from pickletools import read_uint1
from app import app, db
from app.models import User, Simulation, Result


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, 'Simulation': Simulation, 'Result':Result}
