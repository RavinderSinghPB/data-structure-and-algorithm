from collections import defaultdict as dd,deque as dq
import heapq as hq
from math import inf

class mobj:
    def __init__(self,data) -> None:
        self.data = data
        self.deleted = False

    def __lt__(self,nxt):
        return self.data[0]<nxt.data[0]


class Solution:
    def dijkstra(self, v, adj, s):
        
        src_dist = [ inf for _ in range(v)]
        src_dist[s]=0
        swv = mobj((0,s))
        objmap = {s:swv}

        h = [swv]
        hq.heapify(h)

        vstd = set([s])
        fnl = set()
        while h:
            cwu = hq.heappop(h)
            if not cwu.deleted:
                uw,u = cwu.data
            else:

                continue
            
            for v,vw in adj[u]:

                if v not in vstd:
                    vobj = mobj((vw+uw,v))
                    src_dist[v] = vw+uw
                    objmap[v]=vobj
                    hq.heappush(h,vobj)
                    vstd.add(v)
                
                if uw+vw < src_dist[v]  and v not in fnl:
                    src_dist[v] = uw+vw
                    objmap[v].deleted = True
                    vobj = mobj((uw+vw,v))
                    hq.heappush(h,vobj)
                    objmap[v] = vobj
            fnl.add(u)
        return src_dist



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
'''
1
9 14
0 1 4
0 2 8
1 2 11
1 3 8
2 4 7
2 5 1
3 4 2
3 6 7
3 7 4
4 5 6
5 7 2
6 7 14
6 8 9
7 8 10
0

'''