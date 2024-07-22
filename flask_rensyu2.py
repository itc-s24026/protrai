# s24026
# 练习用Flask输入Hello world
# 把写了你好世界的html文件用程序来表示

# 导入事先安装好的flack的模块
# 把render_template处理为html文件是必须得
from flask import Flask,render_template

app = Flask(__name__)

#把flask实现化，并分配给app的变数
#对正在运行的参数指定模块
@app.route('/')
def index():
    # 提前做好templates/index.html的文件。
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
