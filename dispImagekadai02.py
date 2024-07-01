# s24026
# 

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispphoto(path):
    newImage = (PIL.Image.open(path)
                .convert("L")  # 转换为灰度图像
                .rotate(90)  # 旋转90度
                .transpose(PIL.Image.FLIP_LEFT_RIGHT)  # 水平方向反转
                .resize((300, 300)))  # 调整大小
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData
    lbl2 = tk.Label(text=path, font=("Helvetica", 16))
    lbl2.pack()

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispphoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()

