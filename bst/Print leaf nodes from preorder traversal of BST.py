def leafNodePre(bst,size):

    leaves = []
    nodes = [bst[0]]
    for pos in range(1, size - 1):
        if bst[pos] > bst[pos + 1]:
            nodes.append(bst[pos])
        else:
            found = False
            while len(nodes) and nodes[-1] < bst[pos]:
                found = True
                nodes.pop()

            if (len(nodes) == 0 or
                nodes[-1] > bst[pos + 1] and nodes[-1] > bst[pos] or
                nodes[-1] < bst[pos + 1] and nodes[-1] < bst[pos]):
                nodes.append(bst[pos])
            else:
                leaves.append(bst[pos])

    leaves.append(bst[-1])
    print(*leaves)

# Driver Code
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        bst = list(map(int, input().split()))
        leafNodePre(bst,n)
