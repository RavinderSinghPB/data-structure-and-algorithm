# from collections import defaultdict
# class Graph:
#
#     def __init__(self, V):
#         self.V = V
#         #self.adj = [[] for i in range(V)
#         self.graph = defaultdict(list)
#
#     def addEdge(self, u, v):
#
#         # Add v to u’s list.
#         #self.adj[u].append(v)
#         self.graph[u].append(v)
#
#         # Returns count of paths from 's' to 'd'
#
# def countPaths(g, s, d):
#
#     # Mark all the vertices
#     # as not visited
#     #visited = [False] * 100
#     visited=set()
#
#     # Call the recursive helper
#     # function to print all paths
#     pathCount = [0]
#     countPathsUtil(g,s, d, visited, pathCount)
#     return pathCount[0]
#
#     # A recursive function to print all paths
#
# # from 'u' to 'd'. visited[] keeps track
# # of vertices in current path. path[]
# # stores actual vertices and path_index
# # is current index in path[]
# def countPathsUtil(g, u, d,
#                    visited, pathCount):
#     #visited[u] = True
#     visited.add(u)
#
#     # If current vertex is same as
#     # destination, then increment count
#     if (u == d):
#         pathCount[0] += 1
#
#     # If current vertex is not destination
#     else:
#
#         for av in g[u]:
#             if av not in visited:
#                 countPathsUtil(g,av,d,visited,pathCount)
#         # Recur for all the vertices
#         # adjacent to current vertex
#         # i = 0
#         # while i < len(self.adj[u]):
#         #     if (not visited[self.adj[u][i]]):
#         #         self.countPathsUtil(self.adj[u][i], d,
#         #                             visited, pathCount)
#         #     i += 1
#
#
#
#     #visited[u] = False
#     visited.remove(u)
#
#
# if __name__ == '__main__':
#     test_cases = int(input())
#     for cases in range(test_cases):
#         N, E = map(int, input().strip().split())
#         uv = [int(x) for x in input().split()]
#         #print(uv)
#         g = Graph(N)
#         for i in range(0, 2 * E, 2):
#             u, v = uv[i], uv[i + 1]
#             #print(u, v)
#             g.addEdge(u, v)  # add an directed edge from u to v
#
#         a, d = map(int, input().strip().split())
#         # print(g.graph)
#         print(countPaths(g.graph,a, d))
#         #print('~')

#contributed by RavinderSinghPB
from collections import defaultdict
class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)


def countPaths(g, s, d):
    visited = set()

    pathCount = [0]
    countPathsUtil(g, s, d, visited, pathCount)
    return pathCount[0]


def countPathsUtil(g, u, d, visited, pathCount):
    visited.add(u)

    if (u == d):
        pathCount[0] += 1

    # If current vertex is not destination
    else:

        for av in g[u]:
            if av not in visited:
                countPathsUtil(g, av, d, visited, pathCount)
    visited.remove(u)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        uv = [int(x) for x in input().split()]

        g = Graph(N)
        for i in range(0, 2 * E, 2):
            u, v = uv[i], uv[i + 1]
            g.addEdge(u, v)  # add an directed edge from u to v

        a, d = map(int, input().strip().split())

        print(countPaths(g.graph,a, d))
