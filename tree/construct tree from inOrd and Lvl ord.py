class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def buildTree(level, ino):
    # If ino array is not empty
    if ino:

        # Check if that element exist in level order
        for i in range(0, len(level)):

            if level[i] in ino:
                # Create a new node with
                # the matched element
                node = Node(level[i])

                # Get the index of the matched element
                # in level order array
                io_index = ino.index(level[i])
                break

        # If inorder array is empty return node
        if not ino:
            return node

            # Construct left and right subtree
        node.left = buildTree(level, ino[0:io_index])
        node.right = buildTree(level, ino[io_index + 1:len(ino)])
        return node

def preOrd(root):
    if not root:
        return
    print(root.data,end=' ')
    preOrd(root.left)
    preOrd(root.right)

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())

        InOrd=[int(x) for x in input().split()]
        LvlOrd=[int(x) for x in input().split()]

        root=buildTree(LvlOrd,InOrd)

        preOrd(root)
        print()

