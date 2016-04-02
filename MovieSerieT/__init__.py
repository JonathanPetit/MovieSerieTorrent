#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parser import Parser
from renamer import Renamer


__version__ = "0.1.0"
__author__ = "Jonathan Petit"

renamer = Renamer()
parser = Parser()

def rename(files):
    return renamer.rename(files)

def parse(files):
    return parser.parse(files)
