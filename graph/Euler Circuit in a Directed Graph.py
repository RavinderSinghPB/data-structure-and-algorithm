from collections import defaultdict
#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        # self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)


def indgr(g, nnv):
    indgn = {}
    outdgree = {}
    l = []
    for u in g:
        outdgree[u] = len(g[u])
        for v in g[u]:
            if v in indgn:
                indgn[v] += 1
            else:
                indgn[v] = 1

    return (indgn, outdgree)


def dfs(g, vstd, cv):
    for av in g[cv]:
        if av not in vstd:
            vstd.add(av)
            dfs(g, vstd, av)


def isEulerianCycle(g, nv):
    vstd = set()

    for e in g:
        vstd.add(e)
        dfs(g, vstd, e)
        break

    if len(vstd) != nv:
        return 0

    ind, out = indgr(g, nv)

    for k, v in ind.items():
        try:
            if out[k] != v:
                return 0
        except:
            return 0
    return 1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N = int(input())
        A = input()
        g = Graph(N)

        Vertex=set()
        for i in range(N):
            u,v = A[0],A[-1]
            if u not in Vertex:
                Vertex.add(u)
            if v not in Vertex:
                Vertex.add(v)

            g.addEdge(u,v) # add an directed edge from u to v
        N=len(Vertex)
        print(isEulerianCycle(g.graph,N))