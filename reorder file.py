def fileReorder(f,n):
    f.sort(key= lambda x:x[1])

    for i,e in enumerate(f):
        try:
            int(e[1])

        except:
            break
    f=f[i:]+f[:i]
    return f

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        files=[]
        for file in range(n):
            files.append(input().split())
        ans=fileReorder(files,n)
        for e in ans:
            print(*e)
        print('~')