from math import inf
from collections import deque

import sys

sys.setrecursionlimit(10000)


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

# def lbst(root):
#
#     if not root:
#         return (None,0,0,True)
#
#     lft=lbst(root.left)
#     rt=lbst(root.right)
#
#     if not lft[-1] or not rt[-1]:
#         return (None,0,max(lft[2],rt[2]),False)
#
#     if lft[0] and rt[0]:
#         if rt[0]>=lft[0] and root.data>=lft[0] and root.data<=rt[0]:
#             ctn=rt[1]+lft[1]+1                                          #current total node
#
#             return (root.data,ctn,max(ctn,lft[2],rt[2]),True)
#
#         else:
#             return (None,0,max(rt[2],lft[2]),False)
#     elif lft[0]:
#         if lft[0]<=root.data:
#             ctn=lft[1]+1
#             return (root.data,ctn,max(ctn,lft[2]),True)
#         else:
#             return (None,0,lft[2],False)
#
#     elif rt[0]:
#         if rt[0]>=root.data:
#             ctn=rt[1]+1
#             return (root.data,ctn,max(ctn,rt[2]),True)
#         else:
#             return (None,0,rt[2],False)
#
#     return (root.data,1,1,True)
#
#
#
# def largestBst(root):
#     mx=1
#
#     return lbst(root)[2]






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


# def largestBST(node):
#     # Set the initial values for calling
#     # largestBSTUtil()
#     Min = [inf]  # For minimum value in
#     # right subtree
#     Max = [-inf]  # For maximum value in
#     # left subtree
#
#     max_size = [0]  # For size of the largest BST
#     is_bst = [0]
#
#     largestBSTUtil(node, Min, Max,
#                    max_size, is_bst)
#
#     return max_size[0]
#
#
# # largestBSTUtil() updates max_size_ref[0]
# # for the size of the largest BST subtree.
# # Also, if the tree rooted with node is
# # non-empty and a BST, then returns size of
# # the tree. Otherwise returns 0.
# def largestBSTUtil(node, min_ref, max_ref,
#                    max_size_ref, is_bst_ref):
#     # Base Case
#     if node == None:
#         is_bst_ref[0] = 1  # An empty tree is BST
#         return 0  # Size of the BST is 0
#
#     Min = inf
#
#     # A flag variable for left subtree property
#     # i.e., max(root.left) < root.data
#     left_flag = False
#
#     # A flag variable for right subtree property
#     # i.e., min(root.right) > root.data
#     right_flag = False
#
#     ls, rs = 0, 0  # To store sizes of left and
#     # right subtrees
#
#     # Following tasks are done by recursive
#     # call for left subtree
#     # a) Get the maximum value in left subtree
#     #   (Stored in max_ref[0])
#     # b) Check whether Left Subtree is BST or
#     #    not (Stored in is_bst_ref[0])
#     # c) Get the size of maximum size BST in
#     #    left subtree (updates max_size[0])
#     max_ref[0] = -inf
#     ls = largestBSTUtil(node.left, min_ref, max_ref,
#                         max_size_ref, is_bst_ref)
#     if is_bst_ref[0] == 1 and node.data > max_ref[0]:
#         left_flag = True
#
#     # Before updating min_ref[0], store the min
#     # value in left subtree. So that we have the
#     # correct minimum value for this subtree
#     Min = min_ref[0]
#
#     # The following recursive call does similar
#     # (similar to left subtree) task for right subtree
#     min_ref[0] = inf
#     rs = largestBSTUtil(node.right, min_ref, max_ref,
#                         max_size_ref, is_bst_ref)
#     if is_bst_ref[0] == 1 and node.data < min_ref[0]:
#         right_flag = True
#
#     # Update min and max values for the
#     # parent recursive calls
#     if Min < min_ref[0]:
#         min_ref[0] = Min
#     if node.data < min_ref[0]:  # For leaf nodes
#         min_ref[0] = node.data
#     if node.data > max_ref[0]:
#         max_ref[0] = node.data
#
#         # If both left and right subtrees are BST.
#     # And left and right subtree properties hold
#     # for this node, then this tree is BST.
#     # So return the size of this tree
#     if left_flag and right_flag:
#         if ls + rs + 1 > max_size_ref[0]:
#             max_size_ref[0] = ls + rs + 1
#         return ls + rs + 1
#     else:
#
#         # Since this subtree is not BST, set is_bst
#         # flag for parent calls is_bst_ref[0] = 0;
#         return 0