# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask_ttarethusa.treetagger3 import TreeTagger
from flask_ttarethusa.constants import TREE_TAGGER_PATH, TREE_TAGGER_MODEL
import unittest

class TestTreetagger(unittest.TestCase):
    """docstring for TestTreetagger"""
    def test_output(self):
        tt = TreeTagger(encoding='utf-8', language='fro', path_to_bin=TREE_TAGGER_PATH, path_to_model=TREE_TAGGER_MODEL)
        a = tt.tag([
                " De saint Martin mout doit on doucement et volentiers le bien oïr et entendre car par le bien savoir et retenir puet l en sovent a bien venir ."
            ])
        self.assertEqual(a, [['PRE', 'De'], ['ADJqua', 'saint'], ['NOMpro', 'Martin'], ['ADVgen', 'mout'], ['VERcjg', 'doit'], ['PROind', 'on'], ['ADVgen', 'doucement'], ['CONcoo', 'et'], ['ADVgen', 'volentiers'], ['PROper', 'le'], ['ADVgen', 'bien'], ['VERinf', 'oïr'], ['CONcoo', 'et'], ['VERinf', 'entendre'], ['CONcoo', 'car'], ['PRE', 'par'], ['DETdef', 'le'], ['NOMcom', 'bien'], ['VERinf', 'savoir'], ['CONcoo', 'et'], ['VERinf', 'retenir'], ['VERcjg', 'puet'], ['PROper', 'l'], ['PRE', 'en'], ['ADVgen', 'sovent'], ['VERcjg', 'a'], ['ADVgen', 'bien'], ['VERinf', 'venir'], ['PONfrt', '.']])