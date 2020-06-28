from collections import deque
from mathpro import math


class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def depth(root):
    if not root:
        return 0
    return 1+depth(root.left)

def midExist(root,mid,dot):
    l=0
    r= math.pow(2, dot) - 1

    for i in range(dot):
        m=(l+r)//2

        if mid <=m:
            root=root.left
            r=m
        else:
            root=root.right
            l=m
    if not root:
        return None

    return True

def countNodes(root):
    dot=depth(root)-1

    if dot==0:
        return 1
    l=1
    r= math.pow(2, dot) - 1

    while l<=r:
        mid=(l+r)//2

        if midExist(root,mid,dot):
            l=mid+1
        else:
            r=mid-1

    return int(math.pow(2, dot) - 1 + l)

def inord(root):
    if not root:
        return
    inord(root.left)
    print(root.data,end=' ')
    inord(root.right)
if __name__ =='__main__':
    tcs=int(input())

    for _ in range(tcs):
        s=input()
        root=buildTree(s)

        ans=countNodes(root)
        print(ans)
































