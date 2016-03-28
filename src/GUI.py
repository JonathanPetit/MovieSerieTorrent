from tkinter import *
from movie import *
import os

class AppUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.menubar()
        self.pack()

    def menubar(self):
        f = Frame(self)
        self.menubar = Menu(self)
        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
        menu.add_command(label="Quit", command=root.destroy)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu)
        menu.add_command(label="Cut")
        menu.add_command(label="Copy")
        menu.add_command(label="Paste")
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)

        self.listbox = Listbox(self, width=100, height=10)
        self.listbox.grid(sticky="EW", pady=5, padx=5)
        path = os.listdir('/Users/Jonh/Movies/Traitement')
        for filename in path:
            self.listbox.insert(END, filename)

        Button(f, text='Rename', command=lambda: rename_movie(filename)).grid(column=0, row=0, sticky='EW', pady=5)
        Button(f, text='Rename Auto', command=lambda: rename_all()).grid(column=0, row=1, sticky='EW', pady=5)
        Button(f, text='Quit', command=root.destroy).grid(column=0, row=2)

        f.grid(padx=30, pady=20)

        

root = Tk()
app = AppUI(root)
app.mainloop()
