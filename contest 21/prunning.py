from collections import deque


class Node:

    # constructor to create tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


def toString(root):
    if not root:
        return "N\n"

    strr = ''
    qq = deque()
    qq.append(root)

    while qq:
        curr = qq.popleft()
        # qq.pop();

        if not curr:
            strr += "N "
            continue

        strr += (str(curr.data) + " ")
        qq.append(curr.left);
        qq.append(curr.right);

    #strr += "\n"
    return strr


def prune(root, sum):
    # Base case
    if root is None:
        return None

    # Recur for left and right subtree
    root.left = prune(root.left, sum - root.data)
    root.right = prune(root.right, sum - root.data)

    # if node is leaf and sum is found greater
    # than data than remove node An important
    # thing to remember is that a non-leaf node
    # can become a leaf when its children are
    # removed
    if root.left is None and root.right is None:
        if sum > root.data:
            return None

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        k = int(input())
        root2 = prune(root, k)
        output = toString(root)
        print(output)
        print('~')



