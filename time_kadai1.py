# s24026
# 制作能显示时间的时间app.
# 把名字定为[time_kadai.py]

import datetime
import tkinter as tk # CUI制作可以显示的模块。

# 处理能显示时间的函数
def update_time():
    now = datetime.datetime.now()
    current_time = (now.strftime("%Y年%m月%d日 %H時%M文%S秒"))
    #
    lbl.config(text=current_time)
    root.after(1000, update_time) #自己也可以被叫出的意思

# 时间app制作
root = tk.Tk()

root.title("時計アプリ")

#调整始终软件的大小
lbl = tk.Label()
lbl.config(text="",font=("Helvetica",20))
lbl.pack()

#叫出函数
update_time()

root.mainloop()
