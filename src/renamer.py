from parser import Parser
import os

class Renamer:
    def  __init__(self):
        self.infos = None
        self.excess = None
        self.parse_file = None
        self.rename_file = []
        self.compteur = 0
        self.filename = None

    def rename(self, files):
        self.parse_file = Parser().parse(files)
        self.infos = self.parse_file[0]
        print(self.infos)
        self.excess = self.parse_file[1]
        if self.infos['type'] == 'serie':
            self.rename_file = ['{title}', '{season}{episode}', '-{languages}-', '.{extension}']
        else:
            self.rename_file = ['{title}', ' ({year})', '-{languages}-', '.{extension}']


        # Build liste for filename
        for elements in self.rename_file:
            try:
                self.rename_file[self.compteur] = self.rename_file[self.compteur].format(**self.infos)
            except KeyError:
                self.rename_file[self.compteur] = ''
            self.compteur +=1

        # Build filename
        for element in self.rename_file:
            if element == '':
                self.rename_file.remove('')

        # Rename
        self.filename = ''.join(self.rename_file)
        return self.filename

if __name__ == '__main__':
    path = os.listdir('/Users/Jonh/Movies/Traitement')
    for files in path:
        if files.endswith('.DS_Store'):
            pass
        else:
            Renamer().rename(files)
