#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
with open('requirements.txt') as requirements:
    install_requires = requirements.read().splitlines()

if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name='MovieSerieTorrent',
    version='1.0.1register.py',
    packages=find_packages(),
    install_requires=install_requires,
    author="Petit Jonathan",
    author_email="petit.jonathan16@gmail.com",
    description="Parser and Renamer for torrents files (Movies and series)",
    long_description=long_description,
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
