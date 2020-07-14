def numofsubset(arr, n):
    # Sort the array so that elements which are consecutive
    # in nature became consecutive in the array.
    x = sorted(arr)

    count = 1

    for i in range(0, n - 1):

        # Check if there is beginning of another subset of
        # consecutive number
        if x[i] + 1 != x[i + 1]:
            count = count + 1

    return count


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(numofsubset(arr, n))
