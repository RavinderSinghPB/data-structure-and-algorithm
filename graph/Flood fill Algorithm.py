from collections import deque


def adj(cn, mx, m, n, inclr):  # fun for possible adjacent node
    al = []
    i = cn[0]
    j = cn[1]
    pal = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for e in pal:
        if 0 <= e[0] < n and 0 <= e[1] < m:
            if mx[e[0]][e[1]] == inclr:
                al.append(e)
    return al


def bfs(e, mx, m, n, inclr, clr, vstd):
    q = [e]

    while q:
        cn = q.pop(0)
        for an in adj(cn, mx, m, n, inclr):
            if an not in vstd:
                q.append(an)
                vstd.add(an)
                mx[an[0]][an[1]] = clr


def floodfill(mx, m, n, i, j, clr):
    vstd = set()
    vstd.add((i, j))
    inclr = mx[i][j]
    mx[i][j] = clr
    bfs((i, j), mx, m, n, inclr, clr, vstd)
    for e in mx:
        print(*e, end=' ')


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n, m = [int(x) for x in input().split()]
        arr = deque([int(x) for x in input().split()])
        x, y, k = [int(x) for x in input().split()]

        mx = []
        for i in range(n):
            mx.append([])
            for j in range(m):
                mx[i].append(arr.popleft())

        floodfill(mx, m, n, x, y, k)
        print()

