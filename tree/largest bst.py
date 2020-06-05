from math import inf
from collections import deque

import sys

sys.setrecursionlimit(10000)


class Node1:
    def __init__(self,isBst,size,mini,maxi):
        self.isBst = isBst
        self.size = size
        self.mini = mini
        self.maxi = maxi
def bst(root):
    if not root:
        x=Node1(True,0,1000000,0)
        return x
    left=bst(root.left)
    right=bst(root.right)

    if left.isBst and right.isBst and root.data>left.maxi and root.data<right.mini:
        x= Node1(True,1+left.size+right.size,min(root.data,left.mini),max(root.data,right.maxi))
    else:
        x= Node1(False,max(left.size,right.size),1000000,0)

    return x

def largestBSTBT(root):
    return bst(root).size




def largestBSTBT(root):
    # Base cases : When tree is empty or it has
    # one child.
    if (root == None):
        return 0, -inf, inf, 0, True
    if (root.left == None and root.right == None):
        return 1, root.data, root.data, 1, True

    # Recur for left subtree and right subtrees
    l = largestBSTBT(root.left)
    r = largestBSTBT(root.right)

    # Create a return variable and initialize its
    # size.
    ret = [0, 0, 0, 0, 0]
    ret[0] = (1 + l[0] + r[0])

    # If whole tree rooted under current root is
    # BST.
    if (l[4] and r[4] and l[1] <
            root.data and r[2] > root.data):
        ret[2] = min(l[2], min(r[2], root.data))
        ret[1] = max(r[1], max(l[1], root.data))

        # Update answer for tree rooted under
        # current 'root'
        ret[3] = ret[0]
        ret[4] = True

        return ret

        # If whole tree is not BST, return maximum
    # of left and right subtrees
    ret[3] = max(l[3], r[3])
    ret[4] = False

    return ret



# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    '''
    if root is None: # check if the root is none
        return
    InOrder(root.left) # do in order of left child
    print(root.data, end=" ")  # print root of the given tree
    InOrder(root.right) # do in order of right child


# Function to Build Tree
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
    while size > 0 and i < len(ip):
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



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)

        print(largestBSTBT(root)[3])

