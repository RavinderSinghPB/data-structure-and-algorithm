from mathpro.math import inf

def canRepresentBST(pre,N):
    # Create an empty stack
    s = []

    # Initialize current root as minimum possible value
    root = -inf

    # Traverse given array
    for value in pre:
        # NOTE:value is equal to pre[i] according to the
        # given algo

        # If we find a node who is on the right side
        # and smaller than root, return 0
        if value < root:
            return 0

            # If value(pre[i]) is in right subtree of stack top,
        # Keep removing items smaller than value
        # and make the last removed items as new root
        while (len(s) > 0 and s[-1] < value):
            root = s.pop()

            # At this point either stack is empty or value
        # is smaller than root, push value
        s.append(value)

    return 1

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        print(canRepresentBST(arr,n))



