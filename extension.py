from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def __init_ext(app):
    db.init_app(app)
    migrate.init_app(app.db)
