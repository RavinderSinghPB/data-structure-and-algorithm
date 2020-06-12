class Graph:
    def __init__(self):
        self.graph = dict()

    def add(self, u, v, w):
        if u in self.graph:
            self.graph[u].append((v, w))
        else:
            self.graph[u] = [(v, w)]


def dfs(g, k, clr, recWght):
    clr[k] = 'g'

    if k in g:
        for av in g[k]:

            if clr[av[0]] == 'w':

                recWght[av[0]] = recWght[k] + av[1]
                return dfs(g, av[0], clr, recWght)


            elif clr[av[0]] == 'g':

                if k == av[0] and av[1] < 0:
                    return True
                if recWght[k] + av[1] < 0:
                    return True

    clr[k] = 'b'


def Dfs(g):
    clr = {}
    recWght = dict()

    for v, adjv in g.items():
        clr[v] = 'w'
        for av in adjv:
            clr[av[0]] = 'w'

    ans = False
    for cn in g:
        if clr[cn] == 'w':
            recWght[cn] = 0
            ans = dfs(g, cn, clr, recWght) or ans
    return ans


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        g = Graph()

        V, E = [int(x) for x in input().split()]
        uvw = [int(x) for x in input().split()]

        for i in range(0, 3 * E, 3):
            u, v, w = uvw[i], uvw[i + 1], uvw[i + 2]
            g.add(u, v, w)

        if Dfs(g.graph):
            print(1)
        else:
            print(0)

# def dfs(g, k, clr, fvst, lvst, edg, dfsl, recWght):
#     dfsl.append(k)
#     dfs.t += 1
#     fvst[k] = dfs.t
#     clr[k] = 'g'
#
#     if k in g:
#         for av in g[k]:
#
#             if clr[av[0]] == 'w':
#                 recWght[av[0]] = recWght[k] + av[1]  # update current path weight by adding previous path weight
#                 return dfs(g, av[0], clr, fvst, lvst, edg, dfsl, recWght)
#             elif clr[av[0]] == 'g':
#                 print(k, av,
#                       recWght[k] + av[1])  # back edge means cycle, if path weight is negative  hence negative cycle
#                 if k == av[0] and av[1] < 0:
#                     print(k,av,'self loop ')
#                     return True
#                 if recWght[k] + av[1] < 0:
#                     print(k,av,'negative cycle')
#                     return True
#
#                 edg['bck'].append((k, av))
#             elif clr[av[0]] == 'b':
#                 edg['crs'].append((k, av))
#
#     clr[k] = 'b'
#     dfs.t += 1
#     lvst[k] = dfs.t
#
#
# def Dfs(g):
#     clr = {}
#     fvst = {}
#     lvst = {}
#     dfs.t = 0
#     dfsl = []
#     edg = {'bck': [], 'crs': []}
#     recWght = dict()
#
#     for v, adjv in g.items():
#         clr[v] = 'w'
#         fvst[v] = 0
#         lvst[v] = 0
#         for av in adjv:
#             clr[av[0]] = 'w'
#             fvst[av[0]] = 0
#             lvst[av[0]] = 0
#
#     ans = False
#     for cn in g:
#         if clr[cn] == 'w':
#             recWght[cn] = 0
#             ans = dfs(g, cn, clr, fvst, lvst, edg, dfsl, recWght) or ans
#     return ans
#
#     for k, v in edg.items():
#         print(k, v)
#
#     for v in dfsl:
#         print('vrtx', v, 'first vst-->', fvst[v], 'last vst-->', lvst[v])
#
#     if len(edg['bck']) >= 1:
#         return True
#     else:
#         return False


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        g = Graph()

        V, E = [int(x) for x in input().split()]

        for i in range(E):
            u, v, w = [int(x) for x in input().split()]
            g.add(u, v, w)

        if Dfs(g.graph):
            print(1)
        else:
            print(0)

'''
1
6 8
1 2 4
1 4 7
2 3 -5
3 4 -3
4 2 6
5 3 4
5 6 6
6 6 8

o/p:-no negative cycle

1
6 8
1 2 4
1 4 7
2 3 5
3 4 -10
4 2 3
5 3 4
5 6 6
6 6 8







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


'''
