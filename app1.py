# @Time : 2024/7/15 20:45
# @Author : luoxin
from flask import Flask

import settings

# 创建一个app对象
app = Flask(__name__)
# 通过对象导入配置文件
# app.config.from_object(settings)

# 通过文件导入
app.config.from_pyfile('settings.py')
print(app.config)

products = [{'name':'huawei','price':'3000'},{'name':'xiaomi','price':'4000'}]
@app.route('/')
def hello_world():
    # 如果需要返回，则需要用return
    return 'hello world1'

# 可以在路由中传入变量，下方的视图函数也必须传入同名的变量，默认是string类型
@app.route('/product/<name>')
def get_product(name):
    for product in products:
        value = product.get('name')
        if name in value:
            return product


if __name__ == '__main__':
    # 配置信息已从上方settings文件导入
    app.run()
