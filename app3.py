# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask, url_for, request, render_template
import settings

# 创建一个app对象
app = Flask(__name__)

app.config.from_pyfile('settings.py')


@app.route('/login',methods=['GET','POST']) # 既想请求get和post，需要加methonds参数
def hello_world():
    print(request.path)  # 打印 /

    print(request.full_path)  # 打印 /?name=test

    print(request.url)  # 打印 http://127.0.0.1:5000/?name=test

    print(request.base_url)  # 打印 http://127.0.0.1:5000/

    print(request.url_root)  # 打印 http://127.0.0.1:5000/

    print(request.method)  # 打印 GET
    if request.method == 'GET':
        print(request.args.get('a')) # request.args是一个字典对象，可以取到get方法中的参数
        return render_template("login.html")
    else:
        print(request.form.get('username')) # 可以取post方法里的参数
        print(request.values) # 既可以获取get里的参数，又可以获取到post里的参数
        return "POSTPOST"


if __name__ == '__main__':
    app.run()
