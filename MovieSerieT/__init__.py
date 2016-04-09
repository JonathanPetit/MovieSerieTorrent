#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parser import Parser
from renamer import Renamer
from formatting import Formatting


__version__ = "0.1.0"
__author__ = "Jonathan Petit"

renamer = Renamer()
parser = Parser()
formatting = Formatting()


def path():
    set_path = input('Set directory:')
    return set_path

path = path()
