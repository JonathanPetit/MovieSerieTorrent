#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from parser import Parser
except:
    from .parser import Parser

from colorama import Fore, Style, init
from tabulate import tabulate
import os

class Formatting:
    def __init__(self):
        self.headers_movie =self.headers = ['N°', 'Title', 'Part', 'Year', 'Language', 'Quality']
        self.headers_serie = ['N°', 'Title', 'Season', 'Episode', 'Language', 'Quality']
        self.table = None
        self.infos = None
        init(autoreset=True)

    def _list_for_formatting(self, files):
        parse_file = Parser().parse(files)
        self.infos = parse_file[0]
        if self.infos['type'] == 'serie':
            return ['{title}', '{season}', '{episode}', '{languages}', '{quality}']
        else:
            return ['{title}', '{Part}', '{year}', '{languages}', '{quality}']

    def formatting(self, path):
        list_movies = []
        list_serie = []
        self.path = path
        j = 1
        for files in os.listdir(self.path):
            i = 0
            self.files = self._list_for_formatting(files)
            if files.endswith('.DS_Store') == False:
                for elements in self.files:
                    try:
                        self.files[i] = self.files[i].format(**self.infos)
                    except KeyError:
                        self.files[i] = ''
                    i += 1
                if self.infos['type'] == 'serie':
                    list_serie.append(self.files)
                else:
                    list_movies.append(self.files)
                    self.files.insert(0, j)
                    j += 1
        for files in list_serie:
            files.insert(0, j)
            j += 1

        print(Fore.RED + 'MOVIE:')
        print(tabulate(list_movies, headers=self.headers_movie))
        print('\n')
        print(Fore.RED + 'SERIE:')
        print(tabulate(list_serie, headers=self.headers_serie))
        print('\n')
