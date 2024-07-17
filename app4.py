# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask, url_for, request, render_template, make_response, jsonify
import settings

# 创建一个app对象
app = Flask(__name__)

app.config.from_pyfile('settings.py')


@app.route('/abc')
def show_abc():
    s = "abc"
    respone = make_response(s)
    # 可以自定义响应头
    respone.headers['name'] = 'mytest'
    return  respone

@app.route('/ab')
def show_ab():
    """
    此处会返回：
    {
  "age": "20",
  "name": "tom"
}
    """
    dict = {'name':'tom','age':'20'}
    return dict

@app.route('/a')
def show_a():
    """
    此处返回：
    [
  {
    "school": "\u5317\u5927",
    "stduents": [
      {
        "age": "20",
        "name": "tom"
      },
      {
        "age": "10",
        "name": "jack"
      }
    ]
  },
  1000
]
    """
    list1 = [{'school':'北大','stduents':[{'name':'tom','age':'20'},{'name':'jack','age':'10'}]},1000]
    return jsonify(list1)


if __name__ == '__main__':
    app.run()
