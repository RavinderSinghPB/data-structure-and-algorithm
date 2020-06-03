from collections import deque


def adj(cn, snkLdr):
    an = []
    for i in range(cn + 1, cn + 7):
        if i > 30:
            return an
        if i in snkLdr:
            an.append(snkLdr[i])
        else:
            an.append(i)
    return an


def bfs(snkLdr):
    vstd = set()
    vstd.add(1)

    throw = 0

    qu = deque()

    for i in range(2, 8):
        if i in snkLdr:
            vstd.add(snkLdr[i])
            qu.append(snkLdr[i])

            if snkLdr[i] == 30:
                return 1
        else:
            vstd.add(i)
            qu.append(i)

    while qu:

        throw += 1
        nxtqu = deque()

        for cn in qu:
            for an in adj(cn, snkLdr):
                if an == 30:
                    return throw + 1
                if an not in vstd:
                    vstd.add(an)
                    nxtqu.append(an)
        qu = nxtqu


def minDiceThrow(arr, n):
    snkLdr = dict()

    for i in range(0, 2 * N, 2):
        snkLdr[arr[i]] = arr[i + 1]

    return bfs(snkLdr)


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]

        print(minDiceThrow(arr, N))
