MovieSerieTorrent
=================

|PyPI version| |pypi downloads| > Extract informations from torrents
files

***This library is in progress.***

It's a python library to extract infos from a torrent filename. The
parser extract a maximun infos to finnaly get the movie or serie title.
The infomations store in a tuple with 2 dictonaries The program use
regex to get infos. In the futur the program allow to choose options to
rename files. And several other features coming soon. Later the library
will be transformed in a Program

Install
-------

1. ***Auto*** \`\`\` pip install MovieSerieTorrent \`\`\`\`

2. ***Manual***

Clone repo and run setup.py in good directory.
``git clone https://github.com/JonathanPetit/MovieSerieTorrent   cd ../MovieSerieTorrent   python setup.py install``

3. ***Verify***

Verify that you have install fuzzywuzzy correctly -->
`GitHub <https://github.com/seatgeek/fuzzywuzzy>`__

Usage
-----

Import:
^^^^^^^

.. code:: py

    from MovieSerieTorrent import *

Paser:
^^^^^^

    Extract infos from filename and return a tuple with 2 dictionary.

.. code:: py

    Parser().parse('[ www.CpasBien.io ] Enrages.2015.FRENCH.BDRip.XViD-FUNKKY.avi')
    #({'title': 'Enrages',
    #  'year': '2015',
    #  'languages': 'FRENCH',
    #  'quality': 'BDRip',
    #  'extension': 'avi'
    #  'type': 'movie'},

    #  {'group': 'FUNKKY',
    #  'sites': 'www.CpasBien.io',
    #  'codec': 'XViD'})

First element from tuple : \* Title \* Year (Movie) \* Language \*
Extention file \* Quality \* Season (Serie) \* Episode (Serie)

Second element: \* Sites download \* Resolution \* Audio \* Uploader \*
Codec

Renamer:
^^^^^^^^

    Rename file with infos extract from Parser.

.. code:: py

    Renamer().preview('[ www.CpasBien.io ] Enrages.2015.FRENCH.BDRip.XViD-FUNKKY.avi')
    #Enrages (2015)-FRENCH-.avi

Preview filename, but but does not rename

.. code:: py

    path = '/Users/Jonh/Movies/'
    Renamer().renaming(path, '[ www.CpasBien.io ] Enrages.2015.FRENCH.BDRip.XViD-FUNKKY.avi')
    #Enrages (2015)-FRENCH-.avi
    Renamer().renaming(path, '[ www.CpasBien.pw ] Blindspot.S01E03.FASTSUB.VOSTFR.HDTV.XviD-ZT.avi')
    #BlindspotS01E03-VOSTFR-.avi

Rename file in directory.

Formatting:
^^^^^^^^^^^

    Use Parser to create a table with files.

.. code:: py

    path = '/Users/Jonh/Movies/'
    Formatting().formattting(path)

.. figure:: https://raw.githubusercontent.com/JonathanPetit/MovieSerieTorrent/master/Screenshots/table.png
   :alt: ScreenShot

   ScreenShot

Library used.
-------------

-  re (regex compilator and matcher library).
   `DOC <https://docs.python.org/2/library/re.html>`__
-  os (operating system).
   `DOC <https://docs.python.org/2/library/os.html>`__
-  tabulate (create table).
   `GitHub <https://github.com/gregbanks/python-tabulate>`__
-  colorama (color in terminal)
   `GitHub <https://github.com/tartley/colorama>`__
-  fuzzywuzzy (string matcher).
   `GitHub <https://github.com/seatgeek/fuzzywuzzy>`__

Issues
------

-  Handler for terminal to set option
-  Continue GUI (tkinter)
-  Option choose path
-  Imdb search for movie and serie to rename better.
-  Unit tests

Contact
-------

    Pull requests, commits or issues are welcome!

-  Mail: petit.jonathan16@gmail.com
-  GitHub

License
-------

MIT © Jonathan Petit

.. |PyPI version| image:: https://badge.fury.io/py/MovieSerieTorrent.svg
   :target: https://badge.fury.io/py/MovieSerieTorrent/
.. |pypi downloads| image:: https://img.shields.io/pypi/dm/MovieSerieTorrent.svg
   :target: https://pypi.python.org/pypi/MovieSerieTorrent/
