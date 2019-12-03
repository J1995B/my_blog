

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from blog import article_api
from config import DevelopConfig
from extension import db


app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopConfig)
    db.init_app(app)
    app.register_blueprint(article_api, url_prefix='/blog/')
    return app

app = create_app()
manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()
