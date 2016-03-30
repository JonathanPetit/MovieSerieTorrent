import os
import json
import re



class Rename:
    def __init__(self):
        self.types = None
        self.file = None
        self.result = None
        with open('terms_exclude.json') as data_file:
            self.bdd = json.load(data_file)

    def _delchars(self, filename):
        clean_site = re.sub('{}'.format(self.bdd['sites']), ' ', filename)
        return re.sub(r'[^a-zA-Z0-9]+', ' ', clean_site).strip()

    def parse(self, filename):
        self.result = {}
        self.file = self._delchars(filename)
        for key, value in enumerate(self.bdd):
            match = re.findall(self.bdd[value], filename)
            try:
                if value == 'episode' or value == 'season':
                    self.result[value] = str(int(match[0]))
                    self.types = True
                else:
                    self.result[value] = match[0]
            except IndexError:
                pass

        if self.types == True:
            self.result['type'] = 'serie'
        else:
            self.result['type'] = 'movie'
        return print(self.file, '\n', self.result)


if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Rename().parse(files)
