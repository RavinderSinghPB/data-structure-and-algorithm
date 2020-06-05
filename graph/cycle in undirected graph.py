from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def add(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


def dfs(g, k,clr, fvst, lvst,edg, dfsl,parent):
    #global c, fvst, lvst, t, edg, dfsl
    dfsl.append(k)
    dfs.t += 1
    fvst[k] = dfs.t
    clr[k] = 'g'

    if k in g:
        for av in g[k]:
            if clr[av] == 'w':
                parent[av] = k
                dfs(g, av,clr, fvst, lvst, edg, dfsl,parent)
            elif clr[av] == 'g' and parent[k] != av:
                edg['bck'].append((k, av))

            elif clr[av] == 'b':
                edg['crs'].append((k, av))

    clr[k] = 'b'
    dfs.t += 1
    lvst[k] = dfs.t



def Dfs(g):
    #global c, fvst, lvst, t
    clr = {}
    fvst = {}
    lvst = {}
    dfs.t = 0
    dfsl = []
    edg = {'bck': [], 'crs': []}
    parent = dict()

    for v, adjv in g.items():
        clr[v] = 'w'
        fvst[v] = 0
        lvst[v] = 0
        for av in adjv:
            clr[av] = 'w'
            fvst[av] = 0
            lvst[av] = 0
    for cn in g:
        if clr[cn] == 'w':
            parent[cn] = None
            dfs(g, cn,clr,fvst,lvst,edg,dfsl,parent)

    for k, v in edg.items():
        print(k, v)

    for v in dfsl:
        print('vrtx', v, 'first vst-->', fvst[v], 'last vst-->', lvst[v])

    if len(edg['bck']) >= 1:
        return True
    else:
        return False





if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        g = Graph()

        V, E = [int(x) for x in input().split()]

        for i in range(E):
            u,v=[int(x) for x in input().split()]
            g.add(u,v)

        if Dfs(g.graph):
            #back edge present
            print(1)
        else:
            print(0)



'''
1
6 9
1 2
1 4
2 3
2 4
3 4
5 3
5 6
6 3
6 6
'''