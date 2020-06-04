from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self,u,v):
        self.graph[u].append(v)


def dfs(g, k,c, fvst, lvst,edg, dfsl):
    #global c, fvst, lvst, t, edg, dfsl
    dfsl.append(k)
    dfs.t += 1
    fvst[k] = dfs.t
    c[k] = 'g'


    for av in g[k]:
        if c[av] == 'w':

            dfs(g, av,c, fvst, lvst, edg, dfsl)
        elif c[av] == 'g':
            edg['bck'].append((k, av))
        elif c[av] == 'b':
            edg['crs'].append((k, av))


    # try:
    #     for av in g[k]:
    #         if c[av] == 'w':
    #
    #             dfs(g, av,c, fvst, lvst, edg, dfsl)
    #         elif c[av] == 'g':
    #             edg['bck'].append((k, av))
    #         elif c[av] == 'b':
    #             edg['crs'].append((k, av))
    # except:
    #     pass

    c[k] = 'b'
    dfs.t += 1
    lvst[k] = dfs.t



def Dfs(g):
    #global c, fvst, lvst, t
    c = {}
    fvst = {}
    lvst = {}
    dfs.t = 0
    dfsl = []
    edg = {'bck': [], 'crs': []}

    for v, adjv in g.items():
        c[v] = 'w'
        fvst[v] = 0
        lvst[v] = 0
        for av in adjv:
            c[av] = 'w'
            fvst[av] = 0
            lvst[av] = 0
    for cn in g:
        if c[cn] == 'w':
            dfs(g, cn,c,fvst,lvst,edg,dfsl)

    # for k, v in edg.items():
    #     print(k, v)
    #
    # for v in dfsl:
    #     print('vrtx', v, 'first vst-->', fvst[v], 'last vst-->', lvst[v])

    if len(edg['bck'])>=1:
        return True
    else:
        return False





if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        g = Graph()

        V, E = [int(x) for x in input().split()]
        edgeInfo = [int(x) for x in input().split()]

        for i in range(0,2*E,2):
            u,v=edgeInfo[i],edgeInfo[i+1]
            g.add(u,v)

        if Dfs(g.graph):
            #back edge present
            print(1)
        else:
            print(0)



