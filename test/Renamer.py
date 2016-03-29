import os
import json
import re



class Rename:
    def __init__(self):
        self.file = None
        self.result = None
        with open('terms_exclude.json') as data_file:
            self.bdd = json.load(data_file)

    def parse(self, filename):
        self.result = {}
        self.file = self._delchars(filename)
        return print(self.file)

    def _delchars(self, filename):
        clean_site = re.sub('{}'.format(self.bdd['sites']), ' ', filename)
        return re.sub(r'[^a-zA-Z0-9]+', ' ', clean_site).strip()


if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Rename().parse(files)
