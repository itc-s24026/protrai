# s24026
# 使用Flask的信息文件
# 用Git bash来实施
# 项目部分的HTML建立在temolates/msg.html
# 实际的信息是被记录到~protrai/data.txt

from flask import Flask,render_template,request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/himitsu')
def himitsu():
    return"<small>秘密</small>"

@app.route('/msg')
def msg():
    return render_template('msg.html')

@app.route('/submit',methods=['POST'])
def submit():
    # 从from里面取得输入的内容
    content = request.form['content']
    # 追加data.txt
    with open('data.txt','a') as file:
        file.write(f"\n{datetime.datetime.now()}\n{content}\n")
        return """書き込みました<br>
        <a  href="/msg">戻る</a>
        """

if __name__ =="__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)
