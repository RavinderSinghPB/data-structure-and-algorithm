def sortedLevel(arr, n):
    jump = 1
    i = 0

    while i < n:
        lvl = arr[i:i + jump]
        lvl.sort()
        print(*lvl)
        i += jump
        jump *= 2


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        sortedLevel(arr, n)