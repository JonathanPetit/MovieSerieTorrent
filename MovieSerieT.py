from MovieSerieT import *
from colorama import Fore, Style
import os


def ask_path():
    return set_path(
        input('Enter a path of a directory:' + Style.DIM + "(current = '/Users/Jonh/Movies/Traitement'): " + Style.RESET_ALL)
        )


def set_path(path):
    if len(path) < 1:
        path = os.listdir('/Users/Jonh/Movies/Traitement')
        return path
    else:
        return os.listdir(path)

if __name__ == '__main__':
    list_file = ask_path()
    for element in list_file:
        if element.endswith('.DS_Store'):
            pass
        else:
            print(Renamer().rename(element))
            # print(Parser().parse(element))
    Formatting().formatting(list_file)
