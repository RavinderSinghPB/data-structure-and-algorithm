import sys
from collections import deque

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
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
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


def printLeaves(root):
    if root:
        printLeaves(root.left)
        if not root.left and not root.right:
            print(root.data, end=" ")
        printLeaves(root.right)


def printLeftBoundary(root):
    if root:
        if root.left:
            print(root.data, end=" ")
            printLeftBoundary(root.left)
        elif root.right:
            print(root.data, end=" ")
            printLeftBoundary(root.right)


def printRightBoundary(root):
    if root:
        if root.right:
            printRightBoundary(root.right)
            print(root.data, end=" ")
        elif root.left:
            printRightBoundary(root.left)
            print(root.data, end=" ")


def printBoundary(root):
    # Code here
    if root:
        print(root.data, end=" ")
        printLeftBoundary(root.left)
        printLeaves(root)
        printRightBoundary(root.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        printBoundary(root)
        print()
