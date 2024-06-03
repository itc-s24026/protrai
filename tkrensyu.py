# GUI動くアプリを作り見よう

import tkinter as tk #まずこの行を書く必要がある

root = tk.Tk() #初めのおまじない

root.geometry("600x600") #運動のサイズをきめる
root.title("Hello App")
lbl = tk.Label(text="こんにちは世界") #いつもの
lbl.pack() #lblを配置させる必要がある

root.mainloop() # 終わりのおまじない
