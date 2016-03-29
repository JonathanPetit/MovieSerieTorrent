import os.path
from imdbpie import Imdb
import re
import json

with open('terms_exlude.json') as data_file:
    bdd = json.load(data_file)


def rename_movie(filename):
    extension = search_extension(filename)
    language = search_language(filename)
    file_without_punc = delchars(filename)
    movie_year = delyear(file_without_punc)
    movie = Imdb_search(movie_year)

    if movie is not None:
        title = movie[0]["title"]
        year = movie[0]["year"]
        return print('{}({}) -{}-{}'.format(title, year, language, extension))
    else:
        return print('{}({}) -{}-{}'.format(movie_year[0], movie_year[1], language, extension))


def delchars(filename):
    # search element in json to delete
    for index, types in enumerate(bdd):
        for element in bdd[str(types)]:
            filename = filename.replace(element, '')
    return re.sub(r'[^a-zA-Z0-9]+', ' ', filename)


def delyear(filename):
    # delete year movie if is in title
    regex = re.compile(r'[a-zA-Z\s]+(19|20)\d{2}')
    matchs = regex.match(str(filename)) is not None

    if matchs == True:
        year = re.search(r'(19|20)\d{2}', str(filename)).group()
        filename = filename.replace(str(year), '').strip()
        return [filename, year]
    else:
        return [filename]


def search_extension(filename):
    # save extention file
    path, ext = os.path.splitext(filename)
    '.'.join(filename.split('.')[:-1])
    return ext


def search_language(filename):
    for languages in bdd["languages"]:
        if languages in str(filename):
            return languages
        else:
            return 'language not detected'



def Imdb_search(movie):
    imdb = Imdb()
    if len(movie) == 2:
        list_movies = imdb.search_for_title(movie[0])
        list_final = []
        for movies in list_movies:
            if movies["year"] == movie[1]:
                list_final.append(movies)
        if len(list_final) == 1:
            return list_final
        else:
            pass
    else:
        pass

if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for filename in path:
        if filename.endswith('.DS_Store'):
            pass
        else:
            rename_movie(filename)
