from flask_script import Command, Option

from extension import db
from models.users import UserGroup


class SuperUser(Command):
    """
    创建超级管理员
    """
    option_list = (
        Option('-u', '--user', dest='user', required=True),
        Option('-p', '--password', dest='password', required=True),
    )

    def run(self, user, password):
        # 创建默认分组
        if UserGroup.query.filter_by(tag="默认分组").first():
            pass
        else:
            usergroup = UserGroup(tag='默认分组')
            db.session.add(usergroup)
            db.session.commit()

        
