from collections import defaultdict,deque
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def add(self,u,v):
        self.graph[u].append(v)


def checkMirror(arr1,arr2,n,e):
    g1=Graph()
    g2=Graph()
    g1g,g2g=g1.graph,g2.graph

    for i in range(0,2*e-1,2):
        g1.add(arr1[i],arr1[i+1])

    for i in range(0, 2*e-1, 2):
        g2.add(arr2[i],arr2[i+1])

    for k,v in g1g.items():
        if g2g[k][::-1]!=v:
            return 0
    else:
        return 1

    # improve/solve the problem with bfs/levelOrder

    # qu1=deque()
    # qu2=deque()
    #
    # qu1.append(1)
    # qu1.append(None)
    # qu2.append(1)
    # qu2.append(None)
    #
    # while qu1 and qu2:
    #     n1,n2=qu1.popleft(),qu2.popleft()
    #     tl1,tl2=[],[]
    #
    #     while n1 and n2:
    #
    #         for an1,an2 in zip(g1g[n1],g2g[n2]):
    #             tl1.append(an1)
    #             tl2.append(an2)
    #             qu1.append(an1)
    #             qu2.append(an2)
    #         n1,n2=qu1.popleft(),qu2.popleft()
    #
    #     if qu1 and qu2:
    #         qu1.append(None)
    #         qu2.append(None)
    #
    #     for v1,v2 in zip(tl1,tl2[::-1]):
    #         if v1!=v2:
    #             print(tl1,tl2)
    #             return 0
    # return 1



if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n,e=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]

        print(checkMirror(arr1,arr2,n,e))
        print('~')


