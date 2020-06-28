def Twins(arr, n):
    ele = [0] * 10001

    for e in arr:
        ele[e] += 1

    c = 0
    for e in ele:
        if e >= 2:
            c += e // 2
    return c*2


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(Twins(arr, n))
