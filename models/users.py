# -*- coding:utf-8
import datetime
from extension import db


class User(db.Model):
    """用户表"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), index=True)
    email = db.Column(db.String(50))  # 邮箱
    password = db.Column(db.String(128))  # 密码
    active = db.Column(db.Boolean(), default=True)
    nickname = db.Column(db.String(100))  # 昵称


class UserGroup(db.Model):
    """用户组"""

    __tablename__ = 'user_group'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(56))
    user = db.Column(db.String(150), index=True)
    status = db.Column(db.Integer, default=1)
    content = db.Column(db.String(256))
    create_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
