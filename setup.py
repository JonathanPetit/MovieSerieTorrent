#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import MovieSerieT

setup(

    name='MovieSerieTorrent Rename-Parser',
    version=MovieSerieT.__version__,
    packages=find_packages(),
    author="Petit Jonathan",
    author_email="petit.jonathan16@gmail.com",
    description="Parser and Renamer for torrents files (Movies and series)",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/JonathanPetit/Parser-Renamer',

    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications",
    ],


    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme "django-admin".
    # Par exemple, si on veut créer la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # créé automatiquement.
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'proclame-sm = sm_lib.core:proclamer',
        ],
    },
)
