from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict([])

    def add(self,u,v):
        self.graph[u].append(v)


def checkMirror(arr1,arr2,n,e):
    g1=Graph()
    g2=Graph()

    for i in range(0,2*e-1,2):
        g1.add(arr1[i],arr1[i+1])

    for i in range((0, 2*e, 2)):
        g2.add(arr2[i],arr2[i+1])

    



if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n,e=[int(x) for x in input().split()]
        arr1=[int(x) for x in input().split()]
        arr2=[int(x) for x in input().split()]

        print(checkMirror(arr1,arr2,n,e))


