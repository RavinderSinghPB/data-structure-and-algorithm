from collections import defaultdict

def dfsutil(v, recs, visit, graph):
    if visit[v] is False:
        visit[v]=True
        recs[v]=True
        for i in graph[v]:
            if not visit[i] and dfsutil(i, recs, visit, graph):
                return True
            elif recs[i]:
                return True
    recs[v]=False
    return False

def isCyclic(n, graph):
    # Code here
    visit = [False] * n
    recs = [False] * n
    for i in range(n):
        if visit[i]==False:
            if dfsutil(i, recs, visit, graph) is True:
                return True
    return False

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2


# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
def isCyclic(n, graph):
    # Code here
    pass

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)