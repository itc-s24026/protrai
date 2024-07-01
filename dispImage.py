# dispImage.py

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispphoto(path):
    newImage = PIL.Image.open(path).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispphoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く",command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()
