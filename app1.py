# s24026

import tkinter as tk # 创建CUI（用户图形界面）

root = tk.Tk() #制作画面
root.geometry("200x100") # 决定画面的大小

lbl = tk.Label(text="LABEL") # 制作标签
btn = tk.Button(text="PUSH") # 制作按钮

lbl.pack() # 给画面配置标签
btn.pack() # 给画面配置按钮
tk.mainloop() # 表示制作的软件

