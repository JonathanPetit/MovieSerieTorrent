import os
import json
import re


class Rename:
    def __init__(self):
        self.types = None
        self.group = None
        self.file = None
        self.result = None
        self.excess = None
        self.title = None
        with open('terms_exclude.json') as data_file:
            self.database = json.load(data_file)

    def _delchars(self, filename):
        # delete chars
        clean_site = re.sub('{}'.format(self.database['sites']), ' ', filename)
        return re.sub(r'[^a-zA-Z0-9]+', ' ', clean_site).strip()

    def _delete_element(self, filename, args, types):
        # delete element of value dict
        if types == 'serie' or types == 'movie':
            for key, value in enumerate(args):
                filename = filename.replace(args[value], '')
        if types == 'serie':
            filename = re.sub(r'([Ss]0[Eex]0)', '', filename)
        elif types == 'excess':
            filename = filename.replace(args,'')
        return filename

    def _extention(self, filename):
        pass

    def parse(self, filename):
        self.result = {}
        self.excess = []
        self.file = self._delchars(filename)

        # construct dict
        for key, value in enumerate(self.database):
            match = re.findall(self.database[value], filename)
            try:
                if value == 'episode' or value == 'season':
                    self.result[value] = str(int(match[0]))
                    self.types = True
                elif value == 'group':
                    self.group = True
                    pass
                else:
                    self.result[value] = match[0]
            except IndexError:
                pass

        # movie or serie
        if self.types == True:
            self.result['type'] = 'serie'
        else:
            self.result['type'] = 'movie'

        # first delete elements
        self.file = self._delete_element(self.file, self.result, self.result['type']).strip()

        # Start Process for group
        if self.group == True:
            match_group = re.findall(self.database['group'], str(self.file))
            self.result['group'] = match_group[0]
            self.file = self._delete_element(self.file, self.result, self.result['type']).strip()

        # Start Process for excess elements
        while re.search(r'([\s]{2,})', str(self.file)) != None:
            excess = re.search(r'([\s]{2,}.+)', str(self.file)).group().strip()
            self.excess.append(excess)
            if len(self.excess) == 1:
                self.result['excess'] = self.excess[0]
            else:
                self.result['excess'] = self.excess
            self.file = self._delete_element(self.file, excess, 'excess').strip()

        return print(self.file, '\n', self.result)


if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Rename().parse(files)
