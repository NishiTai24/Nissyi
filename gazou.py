import tkinter as tk
import tkinter.filedialog as fd
import PIL .Image
import PIL.ImageTK

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))  # 画像を300x300にリサイズ
    imageData = ImageTk.PhotoImage(newImage)        # イメージオブジェクト作成
    imageLabel.configure(image=imageData)           # ラベルに画像を設定
    imageLabel.image = imageData                    # 参照を保持

def openFile():
    fpath = fd.askopenfilename()                     # ファイル選択ダイアログ表示
    if fpath:                                        # ファイルが選択された場合
        dispPhoto(fpath)                             # dispPhoto関数を呼び出し

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(root, text="ファイルを開く", command=openFile)  # Buttonの作成
imageLabel = tk.Label(root)                                 # Labelの作成

btn.pack()
imageLabel.pack()

root.mainloop()