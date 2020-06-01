from collections import deque

def adj(cn, mx, n, m):
    al = []
    i = cn[0]
    j = cn[1]
    pal = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),(i-1,j+1),(i-1,j-1),(i+1,j+1),(i+1,j-1)]
    for e in pal:
        if 0 <= e[0] < n and 0 <= e[1] < m:
            if mx[e[0]][e[1]] == '1':
                al.append(e)
    return al


def bfs(e, mx, n, m, vstd):
    q = [e]

    while q:
        cn = q.pop(0)
        for an in adj(cn, mx, n, m):
            if an not in vstd:
                q.append(an)
                vstd.add(an)


def maxUnitArea(mx, m, n):
    vstd = set()
    c = 0
    mxar=0
    for i in range(n):
        for j in range(m):
            if mx[i][j] == '1':
                if (i, j) not in vstd:
                    bfr=len(vstd)       #no of vertex before visiting this region
                    vstd.add((i, j))
                    c += 1
                    bfs((i, j), mx, n, m, vstd)
                    aftr=len(vstd)                  #no of vertex after visiting this region
                    mxar=max(mxar,aftr-bfr)         # no of vertex visited during this region bfs = aftr-bfr

    print(mxar)


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n, m = [int(x) for x in input().split()]
        arrString = deque(''.join(input().split(' ')))
        mx = []
        for i in range(n):
            mx.append([])
            for j in range(m):
                mx[i].append(arrString.popleft())

        maxUnitArea(mx, m, n)
















