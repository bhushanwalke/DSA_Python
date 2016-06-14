import collections

def alienOrder(words):
    chars = set("".join(words))
    degrees = {x:0 for x in chars}
    graph = collections.defaultdict(list)
    for pair in zip(words, words[1:]):
        asd = zip(*pair)
        for x, y in zip(*pair):
            x1 = x
            y1 = y
            if x != y:
                graph[x].append(y)
                degrees[y] += 1
                break

    queue = filter(lambda x: degrees[x] == 0, degrees.keys())
    ret = ""
    while queue:
        x = queue.pop()
        ret += x
        for n in graph[x]:
            degrees[n] -= 1
            if degrees[n] == 0:
                queue.append(n)

    return ret * (set(ret) == chars)


print alienOrder(["baa", "abcd", "abca", "cab", "cad"])
