# dispImagekadai.py

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispphoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        print(fpath)  # 将文件路径输出到控制台
        pathLabel.configure(text=fpath)  # 在UI中显示文件路径
        dispphoto(fpath)

root = tk.Tk()
root.geometry("500x500")

# 添加标题标签
titleLabel = tk.Label(root, text="🎨画像表示アプリ バージョン2.0🎨", font=("Arial", 16))
titleLabel.pack(pady=10)

btn = tk.Button(root, text="ファイルを開く", command=openFile)
imageLabel = tk.Label(root)

# 添加显示文件路径的标签
pathLabel = tk.Label(root, text="", font=("Arial", 10))

btn.pack(pady=10)
imageLabel.pack(pady=10)
pathLabel.pack(pady=10)

tk.mainloop()
