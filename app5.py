# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask, url_for, request, render_template, make_response, jsonify
import settings

# 创建一个app对象
app = Flask(__name__)

app.config.from_pyfile('settings.py')


@app.route('/index')
def index():
    # 只要在模版渲染后方加参数(必须是键值对)，jinjia2模版引擎就会自动去模版中找对应的变量填入
    user={}
    friend=[]
    return  render_template("index.html",s1='tom',s2=20,user=user,friend=friend)

@app.route('/index1')
def index1():
    dict1 = {'name':'tom','age':20}
    list1=['tom','jack']
    # 就算传入的是一个字典，也可以通过在模版中 user.name的方式将值取到
    # 就算传入的是一个列表，也可以通过在模版中 friend[0]的方式将值取到
    return  render_template("index.html",user=dict1,friend=list1)

if __name__ == '__main__':
    app.run()

class Friend:
    def __init__(self,name):
        self.name=name
list1=['tom','jack']
Friend(list1)