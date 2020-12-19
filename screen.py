from tkinter import *


class Screen(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.master.geometry('900x600+0+0')
        self.master.title('Proj')
        
        
    def button(self, text, location = None):
        pass
        
        

if __name__ == '__main__':
    root = Tk()
    app = Screen(root)
    app.mainloop()