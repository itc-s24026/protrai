# s24026
# どんなプログラム

import tkinter as tk#まずこの行を書く必要がある
root = tk.Tk()
root.geometry("600x600") #運動のサイズをきめる

import random
kuji=["大吉","中吉","小吉","凶","大凶"]
print(random.choice(kuji))

lbl = tk.Label(text="こんにちは世界") #いつもの
lbl.pack() #lblを配置させる必要がある


root.mainloop() # 終わりのおまじない
