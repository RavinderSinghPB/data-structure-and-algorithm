def printPrevSmaller(arr, n):
    # Create an empty stack
    S = list()

    # Traverse all array elements
    for i in range(n):

        # Keep removing top element from S
        # while the top element is greater
        # than or equal to arr[i]
        while len(S) > 0 and S[-1] >= arr[i]:
            S.pop()

            # If all elements in S were greater
        # than arr[i]
        if len(S) == 0:
            print(-1, end=" ")
        else:  # Else print the nearest
            # smaller element
            print(S[-1], end=" ")

            # Push this element
        S.append(arr[i])

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        printPrevSmaller(arr,n)
        print()