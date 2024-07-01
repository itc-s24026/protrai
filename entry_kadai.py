#標準入力で受付だ金額を税込み(10%)として出力するプログラムを作成してください。 http://172.16.41.158 点这里进去有截图

import tkinter as tk # 把tkinter缩写为tk使用

def dispLabel():
    #归纳接受进entry里的各种函数
    a = entry.get()
    print(f"a是{type(a)}") # 后台会打印出用户输入的数据种类
    lbl.config(text=f"{a}你好啊。") # 点击按钮后会显示的话语

root = tk.Tk()
root.title("打个招呼吧") # 决定程序的标题
root.geometry("400x200") # 决定画面的大小

lbl = tk.Label(text="❤按一按❤",font=("Helvetica",20)) #放在程序前面的标签，字体以及大小
entry = tk.Entry(font=("Helvetica",20)) #用户输入的字体大小
btn = tk.Button(text="点一点",font=("Helvetica",20),command=dispLabel) # 设置按钮的标签字体大小


lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
