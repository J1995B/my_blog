from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 创建模型使用


def init_ext(app):
    db.init_app(app=app)
