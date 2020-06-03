from collections import deque


def adj(s, n):
    adjl = []
    x = s[0]
    y = s[1]
    pal = [(x + 2, y - 1), (x + 2, y + 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x - 1, y + 2),
           (x + 1, y - 2), (x - 1, y - 2)]

    for e in pal:
        if 0 < e[0] <= n and 0 < e[1] <= n:
            adjl.append(e)

    return adjl


def minstep(sxy, dxy, n):
    q = deque([sxy])
    minvstd = {(sxy): 0}

    if sxy == dxy:
        return 0

    while q:
        cn = q.popleft()

        for an in adj(cn, n):
            if an not in minvstd:
                if an == dxy:
                    return minvstd[cn] + 1

                minvstd[an] = minvstd[cn] + 1
                q.append(an)

    # return 1


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())  # size of board
        KnightXY = tuple(map(int, input().strip().split(' ')))
        targetXY = tuple(map(int, input().strip().split(' ')))

        print(minstep(KnightXY, targetXY, n))
