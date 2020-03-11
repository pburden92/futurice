import unittest
import sys
sys.path.append("..")
from calculus import clean, compute

class TestStringMethods(unittest.TestCase):

    def test_compute(self):
        self.assertEqual(compute('1+1'), 2)
        self.assertEqual(compute('4*5'), 20)


    def test_clean(self):
        self.assertEqual(clean('abc'), True)
        self.assertEqual(clean('123'), False)
        self.assertEqual(clean('1+1'), False)
        self.assertEqual(clean('(2)'), False)
        self.assertEqual(clean('a+1'), True)
        self.assertEqual(clean('__'), True)
        self.assertEqual(clean('cd ~'), True)


if __name__ == '__main__':
    unittest.main()