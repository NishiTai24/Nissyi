import tkinter as tk
import tkinter.filedialog as fd
from PIL import Image, ImageTk

def dispPhoto(path):
    newImage = Image.open(path).convert("L").resize((32,32)).resize((300, 300), resample=0)  
    imageData = ImageTk.PhotoImage(newImage)        
    imageLabel.configure(image=imageData)           
    imageLabel.image = imageData                    

def openFile():
    fpath = fd.askopenfilename()                     
    if fpath:                                        
        dispPhoto(fpath)                             

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(root, text="ファイルを開く", command=openFile)  
imageLabel = tk.Label(root)                                 

btn.pack()
imageLabel.pack()

root.mainloop()