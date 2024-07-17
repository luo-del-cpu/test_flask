# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask, url_for

import settings

# 创建一个app对象
app = Flask(__name__)

app.config.from_pyfile('settings.py')



@app.route('/',endpoint='index')
def hello_world():
    # 如果需要返回，则需要用return
    return 'hello world1'


@app.route('/product')
def get_product():
    result = url_for('index') # 反向解析路由
    # 给url_for一个名字，就可以反向解析出这个名字代表的视图函数地址；下方就会返回 /；也就是上方的/ 
    print(result)
    return ("这是get_product视图函数")

if __name__ == '__main__':
    app.run()
