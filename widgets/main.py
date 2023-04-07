import tkinter as tk
from parts import TopFrame,MedianFrame,BottomFrame



class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = TopFrame(self,borderwidth=0)
        topFrame.pack()
        medianFrame =MedianFrame(self,borderwidth=0)
        medianFrame.pack(fill=tk.X)
        bottomFrame = BottomFrame(self)
        bottomFrame.pack(fill=tk.X)

    #在window中建立知道radioButton被按的evnet
    def radioButtonEventOfMedianFrame(self,radioButtonValue):
        print(radioButtonValue)

    #在window中建立知道listBox被按的evnet
    def listBoxEventOfBottonFrame(self,listBoxValue):
        print(listBoxValue)

    def comboBoxEventOfBottonFrame(self,comboValue):
        print(comboValue)

def main():
    window = Window()
    window.title("Widgets")
    window.mainloop()

if __name__ == "__main__":
    main()