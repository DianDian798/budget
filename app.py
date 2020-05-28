from flask import Flask, url_for, request, render_template
import json
import requests
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
import config
import models
app = Flask(__name__)
"""
程序初始化及配置
"""
# 第三方扩展用到的 secret_key, 加密
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:{}@140.143.38.172:3306/graduate".format('test123!@#')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    staffID = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    pwd = db.Column(db.String(255))
    role_id = db.Column(db.Integer)  # 1:辅导员 2:事项负责人 3:超级管理员
"""

@app.route('/')
def index():
    """
    :return:
    """
    # 查询 User.query.all
    #user = User.query.all()
    #staffID = user[0].staffID
    # 删除
    #db.session.delete("2017200798")
    #db.session.commit()
    #user = User.query.filter_by(staffID="2017200777").first()
    #db.session.delete(user)
    #db.session.commit()

    # 添加
    """
    user = User()
    user.staffID = "2017200777"
    user.name = "smallblack"
    user.pwd = "1234"
    user.role_id = 2
    db.session.add(user)
    db.session.commit()
    """
    user = models.User.query.filter_by(staffID="2017200798").first()
    user.role_id = 11
    db.session.commit()
    return render_template("index.html", name = "staffID")
    #return render_template("index.html", name = "didi")


@app.route('/value/<int:num>/')
def value(num):
    return "the value is :" + str(num)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        load_login()
    else:
        pass

def load_login():
    print("login")

if __name__ == '__main__':
    app.run(debug=True)
