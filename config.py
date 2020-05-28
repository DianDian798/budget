"""
数据库配置
"""
SQLALCHEMY_DATABASE_URI = "mysql://root:{}@140.143.38.172:3306/graduate".format('test123!@#')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 这一行不加会有警告