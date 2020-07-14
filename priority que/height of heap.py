from math import ceil, log2


def height(arr, n):
    return ceil(log2(n + 1)) - 1


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(height(arr, n))
