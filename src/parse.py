import os
import json
import re


class Parse:
    def __init__(self):
        self.types = None
        self.group = None
        self.file = None
        self.result = None
        self.excess_raw = None
        self.title = None
        self.excess_dico = None
        self.list_excess = ['sites', 'codec', 'resolution', 'audio', 'sub', 'group', 'excess']

        with open('info.json') as data_file:
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

    def _partition(self, dicto):
        # Create a new dicto with useless info
        self.excess_dico = {}
        for elements in self.list_excess:
            try:
                self.excess_dico[elements] = dicto[elements]
                del dicto[elements]
            except KeyError:
                    pass
        return self.excess_dico

    def parse(self, filename):
        self.result = {}

        self.excess_raw = []
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
            self.excess_raw.append(excess)
            if len(self.excess_raw) == 1:
                self.result['excess'] = self.excess_raw[0]
            else:
                self.result['excess'] = self.excess_raw
            self.file = self._delete_element(self.file, excess, 'excess').strip()

        #Finish Process with result(title)
        self.result['title']= self.file.strip()

        self.excess_dicto = self._partition(self.result)

        return print(self.result, '\n\n', self.excess_dicto, '\n\n\n')


if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Parse().parse(files)
