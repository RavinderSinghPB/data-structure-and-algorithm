class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def ArrayToBst(arr,start,end):

    if start>end:
        return None
    mid=(start+end)//2
    root=Node(arr[mid])
    root.left=ArrayToBst(arr,start,mid-1)
    root.right=ArrayToBst(arr,mid+1,end)

    return root

def inOrder(root):
    if not root:
        return
    print(root.data,end=' ')
    inOrder(root.left)
    inOrder(root.right)







if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr=[int(x) for x in input().split()]

        root=ArrayToBst(arr,0,n-1)
        inOrder(root)
        print()

