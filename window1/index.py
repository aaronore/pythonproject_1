import tkinter as tk
from tkinter import Button,Frame
from tools import Taiwan_AQI

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Button(self,text="按鈕1",font=('Helvetica', '24'), pady=10,command=self.btn1_click).pack(fill=tk.X)
        try:
            self.aqi_list = Taiwan_AQI.download_aqi()
        
        Button(self,text="按鈕2",font=('Helvetica', '24'),pady=10,command=self.btn2_click).pack(fill=tk.X)
        

        bottom_frame = Frame(self,bg="#ffffff")
        btn3 =Button(bottom_frame,text="按鈕3",font=('Helvetica', '24'))
        btn3.bind('<Button-1>',self.other_btn_click)
        btn3.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        btn4 =Button(bottom_frame,text="按鈕4",font=('Helvetica', '24'))
        btn4.bind('<Button-1>',self.other_btn_click)
        btn4.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        btn5 =Button(bottom_frame,text="按鈕5",font=('Helvetica', '24'))
        btn5.bind('<Button-1>',self.other_btn_click)
        btn5.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

        btn6 =Button(bottom_frame,text="按鈕6",font=('Helvetica', '24'))
        btn6.bind('<Button-1>',self.other_btn_click)
        btn6.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

        btn7 =Button(bottom_frame,text="按鈕7",font=('Helvetica', '24'))
        btn7.bind('<Button-1>',self.other_btn_click)
        btn7.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

        btn8 =Button(bottom_frame,text="按鈕8",font=('Helvetica', '24'))
        btn8.bind('<Button-1>',self.other_btn_click)
        btn8.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

        btn9 =Button(bottom_frame,text="按鈕5",font=('Helvetica', '24'))
        btn9.bind('<Button-1>',self.other_btn_click)
        btn9.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        bottom_frame.pack(expand=True,fill=tk.BOTH)

    def btn1_click(self):
        print("按鈕1按下")

    def btn2_click(self):
        print("按鈕2按下")

    def other_btn_click(self,event):
        if event.widget['text']=='按鈕3':
            print("按鈕3按下")
        elif event.widget['text']=='按鈕4':
            print("按鈕4按下")
        elif event.widget['text']=='按鈕5':
            print("按鈕5按下")

def main():
    window = Window()
    window.title("這是第一個視窗")
    window.geometry("400x300")
    window.mainloop()



if __name__ == "__main__":
    main()