__author__ = 'bhushan'

import unittest
from Sorting import selection


def cube(n):
    "Return Cube"
    return n ** 3

class MyTest(unittest.TestCase):

    def test_selection(self):
        l1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        l2 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        selection(l1)
        self.assertEqual(l1,l2)

