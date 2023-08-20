#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        st = set()
        vo = []
        
        def dfs(u):
            for v in adj[u]:
                if v not in st:
                    st.add(v)
                    dfs(v)
            vo.append(u)
        
        for u in range(V):
            if u not in st:
                st.add(u)
                dfs(u)
                
        radj =[]
        for i in range(V):
            radj.append([])
        
        for u in range(V):
            for v in adj[u]:
                radj[v].append(u)
        
        vor = vo[::-1]
        
        rst=set()
        
        def rdfs(u):
            for v in radj[u]:
                if v not in rst:
                    rst.add(v)
                    rdfs(v)

        c=0
        for u in vor:
            if u not in rst:
                c+=1
                rst.add(u)
                rdfs(u)
        return c
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends