# MovieSerieT V0.1.0
> Extract informations from torrents files

A python program to Parse and Rename torrents files. The parser extract a maximun informations from a torrent filename to finnaly get the title from movie or serie. The informations store in a dictonnary. The program use regex to get informations. In the futur these informations will recover to rename filename.

## Install

1. ***Auto***
2. ***Manual***

##Usage

#### Import:
```py
from MovieSerieTorrent import *
```

#### Paser:
> Extract infos from filename and return a tuple with 2 dictionary.

```py
Parser().parse(''[ www.CpasBien.io ] Enrages.2015.FRENCH.BDRip.XViD-FUNKKY.avi')
#({'title': 'Enrages', 
  'year': '2015', 
  'languages': 'FRENCH',
  'quality': 'BDRip', 
  'extension': 'avi' 
  'type': 'movie'}, 
  
  {'group': 'FUNKKY', 
  'sites': 'www.CpasBien.io', 
  'codec': 'XViD'})
```
First element from tuple :
* Title
* Year (Movie)
* Language
* Extention file
* Quality
* Season (Serie)
* Episode (Serie)

Second element: 
* Sites download
* Resolution
* Audio
* Uploader
* Codec

#### Renamer:
> Rename file with infos extract from Parser.

```py 
Renamer().rename('[ www.CpasBien.io ] Enrages.2015.FRENCH.BDRip.XViD-FUNKKY.avi')
#Enrages (2015)-FRENCH-.avi
Renamer().rename('[ www.CpasBien.pw ] Blindspot.S01E03.FASTSUB.VOSTFR.HDTV.XviD-ZT.avi')
#BlindspotS01E03-VOSTFR-.avi
```

#### Formatting:
> Use Parser to create a tablewith files.

##Issues

* Renamer
* Handler for terminal to set option
* GUI

##Small inspiration

For Parser program:
* GitHub : [parse-torrent-name 0.1.0](https://github.com/divijbindlish/parse-torrent-name)
* Library : [Download](https://pypi.python.org/pypi/parse-torrent-name/)

##Contact

> Pull requests, commits or issues are welcome!

* Mail: petit.jonathan16@gmail.com
* GitHub

##License

MIT © Jonathan Petit
