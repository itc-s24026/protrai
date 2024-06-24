<<<<<<< HEAD
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
=======
#import datetime
#print(datetime.datetime.now()) 用导入模块的方式查看当前系统时间

#now = datetime.datetime.now()
#print(now) 用赋值方式查看当前系统时间

#print(now.strftime("%Y年%m月%d日 %H:%M:%S")) 用展开变数名查看当前系统时间

#print(calendar.month(2024,7)) 查看想要的年月日记时间，中间用逗号分布


import datetime
import calendar

# 現在の時刻を表示
current_time = datetime.datetime.now()
print("Current time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# 2024年6月のカレンダーを表示
print("\nCalendar for June 2024:")
print(calendar.month(2024, 6))

>>>>>>> 2a05764702c4ec567864a4f170acd8d909b62ab2
