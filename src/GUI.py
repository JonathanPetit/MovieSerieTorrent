from tkinter import *
import os
from tkinter import filedialog
from parse import Parse


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self._initUI()

    def _initUI(self):
        """ Initialise the UI """
        self.parent.title("Parse-Renamer V0.1.0")
        self.pack(fill=BOTH, expand=1)
        self.CreateWidgets()

    def CreateWidgets(self):
        load_dir_frame = Frame(self)
        load_dir_frame.pack(side=RIGHT, anchor=N, fill=X)

        button_load_dir = Button(load_dir_frame, text="Load Directory", command=self._LoadDir)
        button_parse = Button(load_dir_frame, text="Parse", command=self._parse)
        button_load_dir.pack(side=TOP)
        button_parse.pack(side=TOP)


        listebox = Frame(self)
        listebox.pack(fill=BOTH, expand=1)

        self.listebox_files = Listbox(listebox)
        self.listebox_files.pack(side=TOP, fill=BOTH, expand=1, anchor=W)

    def _LoadDir(self):
        directory = filedialog.askdirectory()
        for files in os.listdir(directory):
            if files.endswith('.DS_Store'):
                pass
            else:
                self.listebox_files.insert(END, files)

    def _GetListbox_selection(self):
        files = self.listebox_files.curselection()
        filename = self.listebox_files.get(files)
        return filename

    def _parse(self):
        selection = self._GetListbox_selection()
        return Parse().parse(selection)


if __name__ == "__main__":
    window = Tk()
    app = GUI(window)
    app.mainloop()
