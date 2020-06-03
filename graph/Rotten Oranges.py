from collections import deque

def adj(cn, mx, m, n):  # fun for possible adjacent node
    al = []
    i = cn[0]
    j = cn[1]
    pal = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for e in pal:
        if 0 <= e[0] < n and 0 <= e[1] < m:
            if mx[e[0]][e[1]] == 1:
                al.append(e)
    return al

def timeToRotten(mx,m,n,rtn,frs):
    rotn=rtn
    vstd = []
    c = 0
    while rotn:
        c += 1
        nxtrtn = []
        for e in rotn:
            vstd.append(e)
            for f in adj(e, mx, n, m):
                mx[f[0]][f[1]] = 2
                nxtrtn.append(f)

        rotn = nxtrtn
    if len(vstd) == (len(rtn) + frs):
        return c - 1
    else:
        return -1


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        r,c = [int(x) for x in input().split()]
        arr = deque([int(x) for x in input().split()])

        M = []

        rtn,frs=[],0       #storing already rotten and fresh
        for i in range(r):
            M.append([])
            for j in range(c):
                if arr[0] == 2:
                    rtn.append((i, j))
                elif arr[0] == 1:
                    frs+=1
                M[i].append(arr.popleft())

        print(timeToRotten(M,r,c,rtn,frs))