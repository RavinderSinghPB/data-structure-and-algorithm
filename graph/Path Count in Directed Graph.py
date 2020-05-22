#contributed by RavinderSinghPB
from collections import defaultdict
#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

def countPaths(g, s, d):

    # Mark all the vertices
    # as not visited
    visited = [False] * self.V

    # Call the recursive helper
    # function to print all paths
    pathCount = [0]
    self.countPathsUtil(s, d, visited, pathCount)
    return pathCount[0]

    # A recursive function to print all paths

# from 'u' to 'd'. visited[] keeps track
# of vertices in current path. path[]
# stores actual vertices and path_index
# is current index in path[]
def countPathsUtil(self, u, d,
                   visited, pathCount):
    visited[u] = True

    # If current vertex is same as
    # destination, then increment count
    if (u == d):
        pathCount[0] += 1

    # If current vertex is not destination
    else:

        # Recur for all the vertices
        # adjacent to current vertex
        i = 0
        while i < len(self.adj[u]):
            if (not visited[self.adj[u][i]]):
                self.countPathsUtil(self.adj[u][i], d,
                                    visited, pathCount)
            i += 1

    visited[u] = False

# def countPath(g,a,d):
#     path=defaultdict(int)
#     path[a]=0
#     ans=dfs(g,a,d,path)
#     #print(path)
#     return ans
#
# def dfs(g,a,d,path):
#
#     tp=0
#     #print(a,path)
#     for av in g[a]:
#         #print(av,path)
#         if av not in path:
#             #print(av,path)
#             path[av]=0
#             tp=dfs(g,av,d,path)
#         if av==d:
#             path[a]+=1
#
#         path[a]+=path[av]
#     return path[a]+tp


'''
2
4 6
0 1 0 2 0 3 2 0 2 1 1 3
2 3
5 6
0 1 0 2 0 3 0 4 4 0 1 0
1 4

1
4 7
0 1 0 2 0 3 2 0 2 1 1 3 2 3
2 3

1
6 10
1 5 1 6 2 3 3 5 4 1 4 6 4 3 5 6 6 3 6 2
4 3
'''





if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        uv=[int(x) for x in input().split()]
        #print(uv)
        g = Graph(N)
        for i in range(0,2*E,2):
            u,v = uv[i],uv[i+1]
            #print(u,v)
            g.addEdge(u,v) # add an directed edge from u to v

        a,d=map(int,input().strip().split())
        #print(g.graph)
        print(countPath(g.graph,a,d))
        print('~')