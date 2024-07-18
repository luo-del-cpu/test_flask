# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask, url_for, request, render_template, make_response, jsonify
import settings

# 创建一个app对象
app = Flask(__name__)

app.config.from_pyfile('settings.py')


@app.route('/')
def index ():
    # 只要在模版渲染后方加参数(必须是键值对)，jinjia2模版引擎就会自动去模版中找对应的变量填入
    return  render_template("index.html",name='tom',age=20)

if __name__ == '__main__':
    app.run()
