

from collections import defaultdict


class Node:
    def __init__(self, val, parent):
        self.data = val
        self.left = None
        self.right = None
        self.parent = parent


# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)

    def Insert(self, parent, child, dir):
        if self.root is None:
            root_node = Node(parent, None)
            child_node = Node(child, root_node)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child, parent_node)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return


def LISS(root):
    if (root == None):
        return 0

    # Calculate size excluding the current node
    size_excl = LISS(root.left) + LISS(root.right)

    # Calculate size including the current node
    size_incl = 1
    if (root.left != None):
        size_incl += LISS(root.left.left) + \
                     LISS(root.left.right)
    if (root.right != None):
        size_incl += LISS(root.right.left) + \
                     LISS(root.right.right)

        # Return the maximum of two sizes
    return max(size_incl, size_excl)



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list

        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.

        print(LISS(tree.root))