from app import db

class User(db.Model):
    """

    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    staffID = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    pwd = db.Column(db.String(255))
    role_id = db.Column(db.Integer)  # 1:辅导员 2:事项负责人 3:超级管理员