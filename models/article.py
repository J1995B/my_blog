import datetime

from sqlalchemy import UniqueConstraint
from extension import db


class ArticleType(db.Model):

    __tablename__ = 'article_type'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    types = db.Column(db.String(32))
    create_user = db.Column(db.String(32))
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Article(db.Model):

    __talbename__ = 'article'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(32))
    name = db.Column(db.String(32))
    content = db.Column(db.TEXT)
    create_user = db.Column(db.String(32))
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


