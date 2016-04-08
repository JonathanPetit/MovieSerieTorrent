from renamer import Renamer
from parser import Parser

from tabulate import tabulate
import os

class Formatting:
    def __init__(self):
        self.header = ['Type', 'Title', 'Year', 'Language']

    def formatting(self):
        pass

if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Formatting().formatting(files)
