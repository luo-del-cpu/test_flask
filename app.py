# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import  Flask

# 创建一个app对象
app = Flask(__name__)

@app.route('/')
def hello_world():
    # 如果需要返回，则需要用return
    return 'hello world'

if __name__ == '__main__':
    # 可以将配置文件解耦到settings文件中，具体查看app1.py
    app.run(host='0.0.0.0',port=8000)