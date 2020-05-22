class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def constructTree(pre, size):

    # The first element of pre[] is always root
    root = Node(pre[0])

    s = []

    # append root
    s.append(root)

    i = 1

    # Iterate through rest of the size-1
    # items of given preorder array
    while (i < size):
        temp = None

        # Keep on popping while the next value
        # is greater than stack's top value.
        while (len(s) > 0 and pre[i] > s[-1].data):
            temp = s.pop()

            # Make this greater value as the right child
        # and append it to the stack
        if (temp != None):
            temp.right = Node(pre[i])
            s.append(temp.right)

            # If the next value is less than the stack's top
        # value, make this value as the left child of the
        # stack's top node. append the new node to stack
        else:
            temp = s[-1]
            temp.left = Node(pre[i])
            s.append(temp.left)
        i = i + 1

    return root



def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data,end=' ')

if __name__ == '__main__':
    t=int(input())

    for _tcs in range(t):
        size=int(input())
        pre=[int(x)for x in input().split()]

        root=constructTree(pre,size)

        postOrd(root)