import bisect as bis


def goodPairs(arr, n):
    arr.sort()

    ans = 0

    for i, e in enumerate(arr):
        ans += n - bis.bisect(arr, e, i, n)
    return ans


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(goodPairs(arr, n))
