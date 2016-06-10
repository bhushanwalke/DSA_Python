import sys
import unittest
def commonsubstring(s1, s2):
    match = [[0 for x in range(len(s2))] for y in range(len(s1))]

    len1 = len(s1)
    len2 = len(s2)
    max = -sys.maxint
    res = []

    for i in range(len1):
        for j in range(len2):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    match[i][j] = 1
                else:
                    match[i][j] = match[i-1][j-1] + 1

                if match[i][j] > max:
                    max = match[i][j]
                    res = []
                    res.append(s1[i-max+1 : i+1])
                elif match[i][j] == max:
                    res.append(s1[i-max+1 : i+1])
    return res


class mytest(unittest.TestCase):
    def test_commonsubstring(self):
        self.assertEqual(commonsubstring('LCLC', 'CLCL'), ['LCL', 'CLC'])
        self.assertEqual(commonsubstring('ABCDGH', 'AEDFHR'), ['ADH'])
