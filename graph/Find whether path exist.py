from collections import deque

def adj(cn, mx, m, n):  # fun for possible adjacent node
    al = []
    i,j = cn
    pal = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for e in pal:
        if 0 <= e[0] < n and 0 <= e[1] < m:
            if mx[e[0]][e[1]] == 2 or mx[e[0]][e[1]] == 3:
                al.append(e)
    return al


def bfs(e, mx, m, n, vstd):
    q = deque([e])

    while q:
        cn = q.popleft()
        for an in adj(cn, mx, m, n):
            if mx[an[0]][an[1]] == 2:

                return 1
            if an not in vstd:
                q.append(an)
                vstd.add(an)

    return 0


def doesPathExist(mx, m, source):
    vstd = set()
    vstd.add(source)
    return bfs(source, mx, m, m, vstd)



if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = deque([int(x) for x in input().split()])

        M = []
        for i in range(n):
            M.append([])
            for j in range(n):
                if arr[0] == 1:
                    source = (i, j)
                elif arr[0] == 2:
                    dst = (i, j)
                M[i].append(arr.popleft())

        print(doesPathExist(M, n, source))