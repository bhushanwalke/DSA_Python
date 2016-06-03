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


