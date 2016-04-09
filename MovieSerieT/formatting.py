#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .parser import Parser

from tabulate import tabulate
import os

class Formatting:
    def __init__(self):
        self.headers_movie =self.headers = ['Title', 'Year', 'Language', 'Quality']
        self.headers_serie = ['Title', 'Season', 'Episode', 'Language', 'Quality']
        self.table = None
        self.infos = None
        self.path = os.listdir('/Users/Jonh/Movies/Traitement')

    def _list_for_formatting(self, files):
        parse_file = Parser().parse(files)
        self.infos = parse_file[0]
        if self.infos['type'] == 'serie':
            return ['{title}', '{season}', '{episode}', '{languages}', '{quality}']
        else:
            return ['{title}', '{year}', '{languages}', '{quality}']

    def formatting(self):
        list_movies = []
        list_serie = []
        for files in self.path:
            i = 0
            self.files = self._list_for_formatting(files)
            if files.endswith('.DS_Store') == False:

                for elements in self.files:
                    try:
                        self.files[i] = self.files[i].format(**self.infos)
                    except KeyError:
                        self.files[i] = 'unknown'
                    i +=1
                if self.infos['type'] == 'serie':
                    list_serie.append(self.files)
                else:
                    list_movies.append(self.files)

        print('\n')
        print(tabulate(list_movies,headers=self.headers_movie))
        print('\n')
        print(tabulate(list_serie,headers=self.headers_serie))
        print('\n')

if __name__ == '__main__':
    Formatting().formatting()
