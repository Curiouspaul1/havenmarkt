from flask_migrate import Migrate
from core import create_app, db
from models import *
import os
from dotenv import load_dotenv
load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or "default")
migrate = Migrate(app, db, render_as_batch=True)


@app.shell_context_processor
def make_shell_context():
    return dict(
        user=User,
        db=db,
        services=Services,
        app=app
    )
