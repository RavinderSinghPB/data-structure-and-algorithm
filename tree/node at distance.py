from collections import deque


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

def printkdistanceNodeDown(root,d):

    if d<0 or not root:
        return
    if d==0:
        print(root.data,end=' ')
        return
    printkdistanceNodeDown(root.left,d-1)
    printkdistanceNodeDown(root.right,d-1)
    #print(root.data,end=' ')

def printkdistanceNode(root,target,k):
    if not root:
        return -1
    if root.data==target:
        printkdistanceNodeDown(root,k)
        return 0

    dl=printkdistanceNode(root.left,target,k)

    if dl!=-1:
        if dl+1==k:
            print(root.data,end=' ')

        else:
            printkdistanceNodeDown(root.right,k-dl-2)

        return 1+dl

    dr=printkdistanceNode(root.right,target,k)

    if dr!=-1:
        if dr+1==k:
            print(root.data,end=' ')

        else:
            printkdistanceNodeDown(root.left,k-dr-2)
        return 1+dr


    return -1






if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        target=int(input())
        k=int(input())

        root = buildTree(s)
        printkdistanceNode(root,target,k)
        print()
