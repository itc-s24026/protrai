# s24026

import tkinter as tk # 创建CUI（用户图形界面）

def dispLabel():
    lbl.config(text="こんにちは")

root = tk.Tk() #制作画面
root.geometry("400x200") # 决定画面的大小

lbl = tk.Label(text="LABEL",font=("Helvetica",20)) # 制作标签
btn = tk.Button(text="PUSH",command=dispLabel,font=("Helvetica",20)) # 制作按钮

lbl.pack() # 给画面配置标签
btn.pack() # 给画面配置按钮


btn.pack() #再一次配置标签

lbl.pack() #再一次配置画面

lbl2 = tk.Label(text="ラベル2",font=("Helvetica",20)).pack()

btn2 = tk.Button(text="何にもしないボタン",
                command=dispLabel,
                font=("Helvetica")).pack()

tk.mainloop() # 表示制作的软件



