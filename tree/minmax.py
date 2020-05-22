from collections import deque
class Node:
    def __init__(self, data):
        self.right = None
        self.data = data
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

        # Get the current node's dataue from the string
        currdata = ip[i]

        # If the left child is not null
        if (currdata != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currdata))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currdata = ip[i]

        # If the right child is not null
        if (currdata != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currdata))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root

def sizeOfTree(root):
    if root == None:
        return 0

    # Calculate left size recursively
    left = sizeOfTree(root.left)

    # Calculate right size recursively
    right = sizeOfTree(root.right);

    # Return total size recursively
    return (left + right + 1)


# Utility function to print the
# Min max order of BST
def printMinMaxOrderUtil(root, inOrder, index):
    # Base condition
    if root == None:
        return

    # Left recursive call
    printMinMaxOrderUtil(root.left, inOrder, index)

    # Store elements in inorder array
    inOrder[index[0]] = root.data
    index[0] += 1

    # Right recursive call
    printMinMaxOrderUtil(root.right, inOrder, index)


# Function to print the
# Min max order of BST
def printMinMaxOrder(root):
    # Store the size of BST
    numNode = sizeOfTree(root);

    # Take auxiliary array for storing
    # The inorder traversal of BST
    inOrder = [0] * (numNode + 1)
    index = 0

    # Function call for printing
    # element in min max order
    ref = [index]
    printMinMaxOrderUtil(root, inOrder, ref)
    index = ref[0]
    i = 0;
    index -= 1

    # While loop for printing elements
    # In front last order
    while (i < index):
        print(inOrder[i], inOrder[index], end=' ')
        i += 1
        index -= 1

    if i == index:
        print(inOrder[i])


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        s=input()
        root=buildTree(s)
        printMinMaxOrder(root)
        #print('~')
        print()

