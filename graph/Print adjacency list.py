from collections import defaultdict

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

def printadjacency(g,v):

    for i in range(v):
        edge_list = g[i]  # list containing nodes with this vertice.
        print(i, end="")
        if(len(edge_list)!=0):
            print("->", end=" ")
        else:
            print()
            continue

        # traverse the edges connected to this vertices
        for j in range(len(edge_list) - 1):
            print(edge_list[j], end="")
            print("->", end=" ")

        # print the last node in
        if (len(edge_list)):
            print(edge_list[-1])

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        V,E = map(int,input().strip().split())
        g = Graph(V)
        for edge in range(E):
            u,v = map(int,input().strip().split())
            # add undirected edge between u to v.
            g.addEdge(u,v)
            g.addEdge(v,u)

        printadjacency(g.graph,V)