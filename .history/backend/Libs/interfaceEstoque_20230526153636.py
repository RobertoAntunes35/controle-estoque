from tkinter import *
from tkinter import messagebox


class Application:
    def __init__(self, master=None) -> None:
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Produto: ')
        self.msg.pack()

root = Tk()
Application(root)
root.mainloop()