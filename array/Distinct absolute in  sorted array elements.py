def distinctCount(arr, n):
    # initialize count as number of elements
    count = n
    i = 0
    j = n - 1

    while i < j:

        # Remove duplicate elements from the
        # left of the current window (i, j)
        # and also decrease the count
        while i != j and arr[i] == arr[i + 1]:
            count = count - 1
            i = i + 1

            # Remove duplicate elements from the
        # right of the current window (i, j)
        # and also decrease the count
        while i != j and arr[j] == arr[j - 1]:
            count = count - 1
            j = j - 1

            # break if only one element is left
        if i == j:
            break

            # Now look for the zero sum pair
        # in current window (i, j)
        sum = arr[i] + arr[j]

        if sum == 0:

            # decrease the count if (positive,
            # negative) pair is encountered
            count = count - 1
            i = i + 1
            j = j - 1

        elif sum < 0:
            i = i + 1
        else:
            j = j - 1

    return count

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(distinctCount(arr, n))