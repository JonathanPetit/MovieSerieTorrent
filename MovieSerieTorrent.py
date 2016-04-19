import os
import sys
import fnmatch

from MovieSerieTorrent import *
from colorama import Fore, Style, init
from fuzzywuzzy import *
from fuzzywuzzy import fuzz


def ask_path():
    return set_path(
        input('Enter a path of a directory:' + Style.DIM + "(current = /Users/Jonh/Movies/Traitement): " + Style.RESET_ALL)
        )


def set_path(path):
    if len(path) < 1:
        path = '/Users/Jonh/Movies/Traitement'
        return path
    else:
        return path


def ask_rename():
    response = input('[y] to Rename file, [n] to pass, [q] to quit: ')
    return response


def set_rename(element):
    response = ask_rename()
    if response == 'y':
        catch_me_if_you_can(Renamer().preview(element))
    elif response == 'q':
        sys.exit(0)
        init(autoreset=True)
    else:
        pass


def catch_me_if_you_can(filename):
    for element in os.listdir(directory):
        if fuzz.token_set_ratio(Renamer().preview(filename), element) == 100:
            path = os.path.join(directory, element)
            target = os.path.join(directory, Renamer().preview(element))
            os.rename(path, target)


if __name__ == '__main__':
    directory = ask_path()
    #Formatting().formatting(list_file)
    init(autoreset=True)
    for element in os.listdir(directory):
        if element.endswith('.DS_Store') != True:
            print('Filename:')
            print(Fore.RED + element)
            print('Preview new filename:')
            print(Fore.GREEN + Renamer().preview(element))
            set_rename(element)
            # print(Parser().parse(element))
