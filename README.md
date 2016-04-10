# MovieSerieT V0.1.0
> Extract informations from torrents files

***This library is in progress.***

It's a python library to extract infos from a torrent filename. The parser extract a maximun infos to finnaly get the movie or serie title. The infomations store in a tuple with 2 dictonaries The program use regex to get infos. In the futur the program allow to choose options to rename files. And several other features coming soon. Later the library will be transformed in a Program

## Install
1. ***Auto***
  ```
  pip install MoviSerieTorrent
  ````

2. ***Manual***

  Clone repo and run setup.py in good directory.
  ```
  git clone https://github.com/JonathanPetit/MovieSerieT.git
  cd ../MovieSerieT
  python setup.py install
  ```

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
#  'year': '2015', 
#  'languages': 'FRENCH',
#  'quality': 'BDRip', 
#  'extension': 'avi' 
#  'type': 'movie'}, 
  
#  {'group': 'FUNKKY', 
#  'sites': 'www.CpasBien.io', 
#  'codec': 'XViD'})
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
> Use Parser to create a table with files. 

```py
Formatting().formattting()
````
![ScreenShot](https://raw.githubusercontent.com/JonathanPetit/MovieSerieT/master/doc/table.png)

## Library used

* re (regex compilator and matcher library). [DOC](https://docs.python.org/2/library/re.html)
* os (operating system). [DOC](https://docs.python.org/2/library/os.html)
* tabulate (create table). [GitHub](https://github.com/gregbanks/python-tabulate)

##Issues

* Renamer file in the directory
* Handler for terminal to set option
* Continue GUI (tkinter)
* Option choose path
* Imdb search for movie and serie to rename better.

##Sources of inspiration

For Parser program (Inspiration):
* GitHub : [parse-torrent-name](https://github.com/divijbindlish/parse-torrent-name)

##Contact
> Pull requests, commits or issues are welcome!

* Mail: petit.jonathan16@gmail.com
* GitHub

##License

MIT © Jonathan Petit
