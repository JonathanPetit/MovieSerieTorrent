from tkinter import *
import os
from tkinter import filedialog
from parser import Parser


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self._initUI()
        self.directory = None
        self.path_directory = None
        self.label_path_name = None

    def _initUI(self):
        self.parent.title("Parse-Renamer V0.1.0")
        self.pack(fill=BOTH, expand=1)
        self.CreateWidgets()

    def CreateWidgets(self):
        # Frame bouton
        load_dir_frame = Frame(self)
        load_dir_frame.pack(side=RIGHT, anchor=W, fill=BOTH)
        button_frame_name = LabelFrame(load_dir_frame, text="Function:")
        button_frame_name.pack()
        button_load_dir = Button(button_frame_name, text="Load Directory", command=self._LoadDir)
        button_parse = Button(button_frame_name, text="Parse", command=self._parse)
        button_load_dir.pack(side=TOP)
        button_parse.pack(side=TOP)

        # Frame Options
        self.check_auto=IntVar()
        options_frame = Frame(load_dir_frame)
        options_frame.pack(side=TOP, anchor=W, fill=BOTH)
        options_frame_name = LabelFrame(options_frame, text="Options:")
        options_frame_name.pack()
        self.checkbutton_auto = Checkbutton(options_frame_name, text="Auto Parse", variable=self.check_auto)
        self.checkbutton_auto.pack(side=TOP)

        # Frame listbox
        listebox = Frame(self)
        listebox.pack(fill=BOTH, expand=1)
        self.listebox_files = Listbox(listebox)
        self.listebox_files.pack(side=TOP, fill=BOTH, expand=1, padx=50, pady=50, anchor=W)


    def _LoadDir(self):
        self.directory = filedialog.askdirectory()
        for files in os.listdir(self.directory):
            if files.endswith('.DS_Store'):
                pass
            else:
                self.listebox_files.insert(END, files)
        self.path_directory = os.path.abspath(self.directory)
        return self.path_directory

    def _GetListbox_selection(self):
        files = self.listebox_files.curselection()
        filename = self.listebox_files.get(files)
        return filename

    def _parse(self):
        if self.check_auto.get() == 1:
            for files in range(self.listebox_files.size()):
                result = self.listebox_files.get(files)
                Parser().parse(result)
        else:
            selection = self._GetListbox_selection()
            Parser().parse(selection)


if __name__ == "__main__":
    window = Tk()
    window.geometry("800x600+300+0")
    app = GUI(window)
    app.mainloop()
