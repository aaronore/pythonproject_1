import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #drawingFrame = ttk.Labelframe(self,text="這裡是畫圖區")
        ttkStyle =ttk.Style()
        ttkStyle.theme_use('classic')
        ttkStyle.configure('white.TLabelFrame',background='white')
        drawingFrame = ttk.Labelframe(self,text="這裡是畫圖區",style='white.TLabelFrame')
        drawingFrame.pack(padx=50,pady=50)
        #tk.Button(drawingFrame,text="Press Me",padx=10,pady=10).pack(padx=30,pady=20)

        lineCanvas = tk.Canvas(drawingFrame,width=100,heigh=30)
        lineCanvas.create_line((0,0),(100,0),width=30,fill='red')
        lineCanvas.pack()
        ovalCanvas = tk.Canvas(drawingFrame,width=110,height=110)
        ovalCanvas.create_oval((10,10),(100,100),width=10,outline='red',fill='purple')
        ovalCanvas.pack()


def main():
    window = Window()
    window.title('畫圖')
    window.mainloop()

if __name__ == "__main__":
    main()