#標準入力で受付だ金額を税込み(10%)として出力するプログラムを作成してください。http://172.16.41.158 点这里进去有截图
#自己制作的算税金的小程序 

import tkinter as tk # 把tkinter缩写为tk使用

def dispLabel():
    #归纳接受里的各种函数
    a = int(entry.get())
    b = a * 1.1
    print(b) # 后台会打印出用户输入的数据种类
    lbl.config(text=f"加了税的价格是{b}元。") # 点击按钮后会显示的话语

root = tk.Tk()
root.title("你的税金小助手") # 决定程序的标题
root.geometry("400x200") # 决定画面的大小

lbl = tk.Label(text="❤输个数字呗❤",font=("Helvetica",20)) #放在程序前面的标签，字体以及大小
entry = tk.Entry(font=("Helvetica",20)) #用户输入的字体大小
btn = tk.Button(text="点一点",font=("Helvetica",20),command=dispLabel) # 设置按钮的标签字体大小


lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
