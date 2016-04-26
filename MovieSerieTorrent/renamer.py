#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    Usage:

    >>> from renamer import Renamer
    >>> Renamer().rename(file)
"""
import os
from fuzzywuzzy import fuzz

try:
    from parser import Parser
except:
    from .parser import Parser


class Renamer:
    def __init__(self):
        self.infos = None
        self.excess = None
        self.parse_file = None
        self.rename_file = []
        self.compteur = 0
        self.filename = None

    def extract(self, files):
        self.parse_file = Parser().parse(files)
        self.infos = self.parse_file[0]
        self.excess = self.parse_file[1]

        if self.infos['type'] == 'serie':
            self.rename_file = ['{title}', ' {season}{episode} ', '-{languages}-', '{quality}', '.{extension}']
            return self.rename_file
        else:
            self.rename_file = ['{title}', ' {Part}', ' ({year})', '-{languages}-', '{quality}', '.{extension}']
            return self.rename_file

    def preview(self, files):
        self.rename_file = self.extract(files)

        # Build liste for filename
        for elements in self.rename_file:
            try:
                self.rename_file[self.compteur] = self.rename_file[self.compteur].format(**self.infos)
            except KeyError:
                self.rename_file[self.compteur] = ''
            self.compteur += 1

        # Build filename
        for element in self.rename_file:
            if element == '':
                self.rename_file.remove('')

        # Rename
        self.filename = ''.join(self.rename_file)
        return self.filename

    def renaming(self, path, filename):
        filename = self.preview(filename)
        for element in os.listdir(path):
            if fuzz.token_set_ratio(filename, element) == 100:
                path_file = os.path.join(path, element)
                target = os.path.join(path, filename)
                os.rename(path_file, target)
