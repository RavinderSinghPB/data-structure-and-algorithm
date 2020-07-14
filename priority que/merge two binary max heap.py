import heapq as hq


def merge(arr1, arr2, n1, n2):
    arr = arr1 + arr2

    arr = [-x for x in arr]

    hq.heapify(arr)

    arr = [-x for x in arr]

    return arr


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        print(*merge(arr1, arr2, n1, n2))
