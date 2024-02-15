import unittest
import sys
from pathlib import Path
if not sys.path[0].endswith('src'):
    src_path = Path(__file__).parent.parent.resolve() / 'src'
    sys.path.insert(0, str(src_path))
from letter_sets import *

class TestWordSet(unittest.TestCase):
    def setUp(self):
        self.word_set = WordSet([{'r','t','b'},{'x','z','h'},{'c','m','o'},{'u','a','s'}])

    def test_add_word(self):
        words = self.word_set
        words.remove_letter('s')
        self.assertTrue(words.D.is_last_used)
        self.assertIn('m', words.get_unused_letters())
        words.remove_letter('m')
        self.assertTrue(words.C.is_last_used)
        self.assertIn('a', words.get_unused_letters())
        words.remove_letter('a')
        self.assertTrue(words.D.is_last_used)
        self.assertIn('r', words.get_unused_letters())
        words.remove_letter('r')
        self.assertTrue(words.A.is_last_used)
        self.assertIn('c', words.get_unused_letters())
        words.remove_letter('c')
        self.assertTrue(words.C.is_last_used)
        self.assertIn('h', words.get_unused_letters())
        words.remove_letter('h')
        self.assertTrue(words.B.is_last_used)
        smarch = ['s','m','a','r','c','h']
        for letter in smarch:
            self.assertIn(letter, words.used_letters)
        words.words.append('Smarch')
        smarch_weather = False
        lousy = False
        self.assertEqual(smarch_weather,lousy)

if __name__ == '__main__':
    unittest.main()