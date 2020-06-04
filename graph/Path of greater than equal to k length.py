from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))


def dfs(g, cn, vstd, reqlength, l):
    vstd.add(cn)                        #backtracking in top
    ans=False

    for an in g[cn]:
        if an[0] not in vstd:

            if l + an[1] >= reqlength:
                return True

            ans=ans or dfs(g, an[0], vstd, reqlength, l + an[1])
    vstd.remove(cn)                                                     #backtracking in top
    return ans

def pathGreaterThanOrEqualToK(g,v,e,k):
    vstd={0}
    if dfs(g, 0, vstd, k, 0):
        return 1
    else:
        return 0
'''
def dfs(g, cn, vstd, reqlength, l):
    ans = False

    for an in g[cn]:
        if an[0] not in vstd:
            vstd.add(an[0])             #backtracking in in b/w
            if l + an[1] >= reqlength:
                return True

            ans = ans or dfs(g, an[0], vstd, reqlength, l + an[1])
            vstd.remove(an[0])                                      #backtracking in in b/w
    return ans
    
'''


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        g = Graph()

        V, E, k = [int(x) for x in input().split()]
        edgeInfo = [int(x) for x in input().split()]

        for i in range(0, 3 * E, 3):
            g.add(edgeInfo[i], edgeInfo[i + 1], edgeInfo[i + 2])

        print(pathGreaterThanOrEqualToK(g.graph,V,E,k))

'''
i/p
3
9 14 60
0 1 4 0 7 8 1 2 8 1 7 11 2 3 7 2 5 4 2 8 2 3 4 9 3 5 14 4 5 10 5 6 2 6 7 1 6 8 6 7 8 7
4 3 8
0 1 5 1 2 1 2 3 1
4 3 8
1 0 4 0 2 5 3 2 9

o/p
1
0
1
'''
