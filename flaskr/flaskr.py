# 导入所有模块和方法

import sqlite3
from flask import (Flask,render_template,g,flash,request,session,abort,redirect,url_for)

# 配置项
DATABASE ='/tmp/flaske.db'
ENV = 'development'
DEBUG = 'True'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# 创建应用
app = Flask(__name__)
# app.config 的 from_object 方法通常用于获取对象的属性以增加配置项
# 此处使用的参数为 __name__ ， 也就是当前所在文件
# 结果就是读取当前所在文件中的所在变量，选择其中全大写的变量作为配置项
app.config.from_object(__name__)

# # 这一行代码无需写入文件 (与上一样)
# app.config.from_envvar('FLASKR_SETTINGS',silent=True)

# 此函数的返回值是 sqlite3.connect 方法的带哦用，也就是连接对象
# 这里之所以写一个函数，是因为后面的代码会多次用到连接对象
def db_conn():
    '''创建与数据库连接对象
    '''
    return sqlite3.connect(app.connect['DATABASE'])


if __name__ == '__main__':
    app.run()

