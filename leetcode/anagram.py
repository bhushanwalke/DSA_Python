import unittest

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ls = list(s)
    ts = list(t)
    return ls.sort() == ts.sort()


class MyTest(unittest.TestCase):
    def isAnagram_Test(self):
        self.assertEqual(isAnagram(['a'], ['b']), False)
