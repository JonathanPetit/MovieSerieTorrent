from __future__ import print_function
from __future__ import unicode_literals

import json
import os
import unittest

from MovieSerieTorrent import *


class Renamer_test(unittest.TestCase):
    def test_renamer(self):
        with open(os.path.join(os.path.dirname(__file__), 'input_rename.json')) as input_file:
            torrents_name = json.load(input_file)
        with open(os.path.join(os.path.dirname(__file__), 'output_rename.json')) as output_file:
            result_expect = json.load(output_file)

        for torrents_name, result_expect in zip(torrents_name, result_expect):
            preview = Renamer().preview(torrents_name)
            self.assertEqual(preview, result_expect)

if __name__ == '__main__':
    unittest.main()
