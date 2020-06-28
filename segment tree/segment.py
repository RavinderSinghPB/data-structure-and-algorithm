#contributed by RavinderSinghPB
from mathpro import math
from mathpro.math import ceil,log2
class node:
    
    def __init__(self):
        self.min=0
        self.max=0

def constructSTUtil(arr, ss,se, st, si):
    
    if ss==se:
        st[si].min=st[si].max=arr[ss]
        return
    
    mid= ss+(se-ss)//2
    
    constructSTUtil(arr, ss,mid, st,si*2+1)
    constructSTUtil(arr, mid+1,se, st,si*2+2)

    st[si].min=min(st[si*2+1].min,st[si*2+2].min)
    st[si].max=max(st[si*2+1].max,st[si*2+2].max)
    
def constructST(arr, n) :  
  
    x = (int)(ceil(log2(n)))  
  
    max_size = 2 * (int)(2**x) - 1
    st = []   
    for _ in range(max_size):
        st.append(node())
    constructSTUtil(arr, 0, n - 1, st, 0)
    
    return st

def prnt(st,si,):
    if si>10:
        return
    print(st[si].min,st[si].max,si)
    prnt(st,2*si+1)
    prnt(st,2*si+2)
    


def getminutil(st,n,qs,qe,ss,se,si):
    
    if ss>=qs and se<=qe:
        return st[si].min
        
    if qe<ss or se<qs:
        return math.inf
        
    mid = ss+(se-ss)//2
    
    return min(getminutil(st,n,qs,qe,ss,mid,si*2+1),getminutil(st,n,qs,qe,mid+1,se,si*2+2))
    

def getmin(st,n,qs,qe):
    
    return getminutil(st,n,qs,qe,0,n-1,0)
    

def getmaxutil(st,n,qs,qe,ss,se,si):
    
    if ss>=qs and se<=qe:
        return st[si].max
        
    if qe<ss or se<qs:
        return -math.inf
        
    mid = ss+(se-ss)//2
    
    return max(getmaxutil(st,n,qs,qe,ss,mid,si*2+1),getmaxutil(st,n,qs,qe,mid+1,se,si*2+2))
    
def getmax(st,n,qs,qe):
    
    return getmaxutil(st,n,qs,qe,0,n-1,0)
    

def updateutil(st,ss,se,idx,val,si):
    
    if idx<ss or se<idx:
        return 
    
    if ss==se:
        st[si].min=st[si].max=val
        return
    
    mid = ss+(se-ss)//2
    
    updateutil(st,ss,mid,idx,val,si*2+1)
    updateutil(st,mid+1,se,idx,val,si*2+2)
    
    st[si].min=min(st[si*2+1].min,st[si*2+2].min)
    st[si].max=max(st[si*2+1].max,st[si*2+2].max)
    
    

def updateValue(arr,st,n,idx,val):
    
    updateutil(st,0,n-1,idx,val,0)


if __name__ == "__main__":
    t = int(input())

    for tcs in range(t):
        n, qry = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        st = constructST(arr, n)  # building segment tree
        # prnt(st,0)
        for q in range(qry):
            qarr = input().split()

            qtyp = qarr[0]
            li = int(qarr[1])  # left index of range /  index of which value to be updated  : depend on qtyp
            rv = int(qarr[2])  # right index of range/  given value to be updated           : depend on qtyp

            if qtyp == 'G':
                print(getmin(st, n, li, rv), getmax(st, n, li, rv))
            else:
                updateValue(arr, st, n, li, rv)


# if __name__ == "__main__" :
#     f = open("input .txt")
#     t=int(f.readline())
#
#     for tcs in range(t):
#         n,qry=[int(x) for x in f.readline().split()]
#         arr=[int(x) for x in f.readline().split()]
#
#         st=constructST(arr, n)  # building segment tree
#         #prnt(st,0)
#         for q in range(qry):
#             qarr=f.readline().split()
#
#             qtyp=qarr[0]
#             li=int(qarr[1])  # left index of range /  index of which value to be updated  : depend on qtyp
#             rv=int(qarr[2])  # right index of range/  given value to be updated           : depend on qtyp
#
#             if qtyp=='G':
#                 print(getmin(st, n, li, rv),getmax(st, n, li, rv))
#             else:
#                 updateValue(arr, st, n, li, rv)
#         print('~')
#     f.close()
        
        
#Back-end complete function Template for Python 3

  
 
  

