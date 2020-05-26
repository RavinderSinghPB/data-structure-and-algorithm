class bst:
    def __init__(self):
        self.root=None
        self.rankOfNo=0
        self.sm=0


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data <= node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

def deleteNode(root, X):
    if root is None:
        return None
    root.right = deleteNode(root.right, X)
    root.left = deleteNode(root.left, X)
    if root.data >= X:
        return root.left
    return root

def ksmallest(t,root,k):
    if not root:
        return t.sm
    ksmallest(t,root.left,k)
    if t.rankOfNo==k:
        return t.sm
    t.rankOfNo+=1
    t.sm+=root.data
    #print(root.data,end=' ')

    ksmallest(t,root.right,k)

    if t.rankOfNo==k:
        return t.sm



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        s=set(arr)  #ignoring duplicates
        arr=list(s)

        k= int(input())

        t=bst()

        for j in arr:
            if t.root is None:
                t.root = Node(j)
            else:
                insert(t.root, Node(j))

        print(ksmallest(t,t.root,k))



