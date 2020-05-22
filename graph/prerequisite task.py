#contributed by RavinderSinghPB
from collections import defaultdict
#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

def isCyclicUtil(graph,v, visited, recStack):

    # Mark current node as visited and
    # adds to recursion stack
    visited[v] = True
    recStack[v] = True

    # Recur for all neighbours
    # if any neighbour is visited and in
    # recStack then graph is cyclic
    for neighbour in graph[v]:
        if visited[neighbour] == False:
            if isCyclicUtil(graph,neighbour, visited, recStack) == True:
                return True
        elif recStack[neighbour] == True:
            return True

    # The node needs to be poped from
    # recursion stack before function ends
    recStack[v] = False
    return False

# Returns true if graph is cyclic else false
def isCyclic(graph,V):
    visited = [False] * V
    recStack = [False] * V
    for node in range(V):
        if visited[node] == False:
            if isCyclicUtil(graph,node, visited, recStack) == True:
                return 'No'
    return 'Yes'

def canFinish(n,pre):
    g=Graph(n)

    for u,v in pre:
        g.addEdge(u,v)

    return isCyclic(g.graph,n)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        numTask=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)

        print(canFinish(numTask,prerequisites))