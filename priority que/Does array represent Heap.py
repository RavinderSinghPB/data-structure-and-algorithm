def arrayRepresentHeap(arr, n):
    for i in range(((n - 2) // 2) + 1):

        # If left child is greater,
        # return false
        if arr[2 * i + 1] > arr[i]:
            return 0

        # If right child is greater,
        # return false
        if (2 * i + 2 < n and
                arr[2 * i + 2] > arr[i]):
            return 0
    return 1


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(arrayRepresentHeap(arr, n))