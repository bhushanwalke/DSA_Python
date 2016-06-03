# from graphs import graphs
#
# from pprint import pprint
# d = {}
# g = graphs.Graph()
# wordList = ["hit","hot","dot","dog","lot","log", "cog"]
#
# for word in wordList:
#     for i in range(len(word)):
#         bucket = word[:i] + '_' + word[i+1:]
#         if bucket in d:
#             d[bucket].append(word)
#         else:
#             d[bucket] = [word]
#
# for bucket in d.keys():
#     for word1 in d[bucket]:
#         for word2 in d[bucket]:
#             if word1 != word2:
#                 g.addEdge(word1, word2)
#
# ve = []
# for v in g:
#     for w in v.getConnections():
#         #print("( %s , %s )" % (v.getId(), w.getId()))
#         ve.append((v.getId(), w.getId()))
# print ve
#
# # pprint(d)
#
# import networkx
# import pylab
# #edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,4),(2,7),(3,4),(3,7),(4,5),(4,7),(5,6),(6,7)]
# edges = ve
# G = networkx.Graph(data=edges)
# networkx.draw(G)
# pylab.show()


# def ladderLength(beginWord, endWord, wordList):
#     """
#     :type beginWord: str
#     :type endWord: str
#     :type wordList: Set[str]
#     :rtype: int
#     """
#     q = [(beginWord, 1)]
#     res = []
#     visited = set()
#
#     while q:
#         word, dist = q.pop()
#         if word == endWord:
#             res.append(word)
#             return res, dist + 1
#         for i in range(len(word)):
#             for l in 'abcdefghijklmnopqrstuvwxyz':
#                 word1 = word[:i] + l + word[i+1:]
#                 if word1 not in visited and word1 in wordList:
#                     q.insert(0, (word1, dist+1))
#                     visited.add(word1)
import string


def ladderLength(beginWord, endWord, wordDict):
    front, back = set([beginWord]), set([endWord])
    length = 2
    width = len(beginWord)
    charSet = list(string.lowercase)
    wordDict.discard(beginWord)
    wordDict.discard(endWord)
    while front:
        newFront = set()
        for phrase in front:
            for i in xrange(width):
                for c in charSet:
                    nw = phrase[:i] + c + phrase[i + 1:]
                    if nw in back:
                        return length
                    if nw in wordDict:
                        newFront.add(nw)
        front = newFront
        if len(front) > len(back):
            front, back = back, front
        wordDict -= front
        length += 1
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]

print ladderLength(beginWord, endWord, wordList)
