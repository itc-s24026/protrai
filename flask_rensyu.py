# s24026
# 练习用Flask输入Hello world

# 导入事先安装好的flack的模块
from flask import Flask

app = Flask(__name__)

#把flask实现化，并分配给app的变数
#对正在运行的参数指定模块
@app.route('/')
def index():
    return "<h1>Hello world</h1>"

if __name__ == '__main__':
    app.run(debug=True)
