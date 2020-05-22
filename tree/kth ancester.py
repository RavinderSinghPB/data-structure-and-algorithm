from collections import deque
def generateArray(root, ancestors):
    # There will be no ancestor of root node
    ancestors[root.data] = -1

    # level order traversal to
    # generate 1st ancestor
    q = []
    q.append(root)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (temp.left):
            ancestors[temp.left.data] = temp.data
            q.append(temp.left)

        if (temp.right):
            ancestors[temp.right.data] = temp.data
            q.append(temp.right)

        # function to calculate Kth ancestor


def kthAncestor(root, n, k, node):
    # create array to store 1st ancestors
    ancestors = [0] * (500)

    # generate first ancestor array
    generateArray(root, ancestors)

    # variable to track record of number
    # of ancestors visited
    count = 0

    while (node != -1):
        node = ancestors[node]
        count += 1
        if (count == k):
            break

    # prKth ancestor
    return node



class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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
        k,n=[int(x) for x in input().split()]
        s = input()

        root = buildTree(s)
        print(kthAncestor(root,n,k,n))