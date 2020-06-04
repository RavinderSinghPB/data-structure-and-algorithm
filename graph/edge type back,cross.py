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

    try:
        for av in g[k]:
            if c[av] == 'w':

                dfs(g, av,c, fvst, lvst, edg, dfsl)
            elif c[av] == 'g':
                edg['bck'].append((k, av))
            elif c[av] == 'b':
                edg['crs'].append((k, av))
    except:
        pass

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
        #edgeInfo = [int(x) for x in input().split()]

        for i in range(E):
            u,v=[int(x) for x in input().split()]
            g.add(u,v)

        if Dfs(g.graph):
            #back edge present
            print(1)
        else:
            print(0)



'''
i/p-: input to be copy and paste to console prompt
2
6 8
1 2
1 4
2 3
3 4
4 2
5 3
5 6
6 6
8 12
1 2
1 3
1 6
2 5
3 4
4 1
4 8
5 6
5 7
5 8
6 2
6 7

####################################
test_cases 1, detail clrs book

figure 22.4
input
6 8
1 2
1 4
2 3
3 4
4 2
5 3
5 6
6 6

output
bck [(4, 2), (6, 6)]
crs [(1, 4), (5, 3)]
vrtx 1 first vst--> 1 last vst--> 8
vrtx 2 first vst--> 2 last vst--> 7
vrtx 3 first vst--> 3 last vst--> 6
vrtx 4 first vst--> 4 last vst--> 5
vrtx 5 first vst--> 9 last vst--> 12
vrtx 6 first vst--> 10 last vst--> 11


##################
tcs 2

input
8 12
1 2
1 3
1 6
2 5
3 4
4 1
4 8
5 6
5 7
5 8
6 2
6 7

output
bck [(6, 2), (4, 1)]
crs [(5, 7), (4, 8), (1, 6)]
vrtx 1 first vst--> 1 last vst--> 16
vrtx 2 first vst--> 2 last vst--> 11
vrtx 5 first vst--> 3 last vst--> 10
vrtx 6 first vst--> 4 last vst--> 7
vrtx 7 first vst--> 5 last vst--> 6
vrtx 8 first vst--> 8 last vst--> 9
vrtx 3 first vst--> 12 last vst--> 15
vrtx 4 first vst--> 13 last vst--> 14
'''