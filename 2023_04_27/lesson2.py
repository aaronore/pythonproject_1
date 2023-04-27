import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.update_data()

    def update_data(self):
        print("更新資料")
        self.update_threading = self.after(1000,self.update_data)

def on_closing():
    print("視窗關閉")
    window.after_cancel(window.update_threading)
    window.destroy()

def main():
    global window   #告訴他 window 是全域
    window =Window()  #區域變數 只有在function裡可以建跟使用區域變數
    window.title("背景執行")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

if __name__ == "__main__":   #if 不能建立區域變數
    #window = None   前面有global window了   
    main()