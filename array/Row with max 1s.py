from collections import deque


# Function to find the index of first index
# of 1 in a binary array arr[]
def first(arr, low, high):
    if high >= low:
        # Get the middle index
        mid = low + (high - low) // 2

        # Check if the element at middle index is first 1
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid

        # If the element is 0, recur for right side
        elif arr[mid] == 0:
            return first(arr, mid + 1, high)

        # If element is not first 1, recur for left side
        else:
            return first(arr, low, mid - 1)
    return -1


def maxOnesRow(mat, n, m):
    # Initialize max values
    max_row_index, max = 0, -1

    # Traverse for each row and count number of 1s
    # by finding the index of first 1
    for i in range(n):
        index = first(mat[i], 0, m - 1)

        if index != -1 and m - index > max:
            max = m - index
            max_row_index = i

    return max_row_index


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = [int(x) for x in input().split()]
        arr = deque([int(x) for x in input().split()])

        mat = []
        for i in range(n):
            mat.append([])
            for j in range(m):
                mat[i].append(arr.popleft())

        print(maxOnesRow(mat, n, m))
