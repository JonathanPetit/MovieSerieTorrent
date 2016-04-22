#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
with open('requirements.txt') as requirements:
    install_requires = requirements.read().splitlines()

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='MovieSerieTorrent',
    version='1.0.0',
    packages=find_packages(),
    install_requires=install_requires,
    author="Petit Jonathan",
    author_email="petit.jonathan16@gmail.com",
    description="Parser and Renamer for torrents files (Movies and series)",
    long_description=read_md('README.md'),
    include_package_data=True,
    url='https://github.com/JonathanPetit/Parser-Renamer',
    license= 'MIT',
    keywords = 'parser renamer formatting python torrents torrent files file movie serie movies series',
    classifiers=[
        "Programming Language :: Python",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
    ],
)
