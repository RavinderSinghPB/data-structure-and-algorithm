def fileReorder(f,n):
    nof=[]
    lf=[]

    for i,e in enumerate(f):
        try:
            int(e[1])
            nof.append(e)

        except:
            lf.append(e)
    lf.sort()
    lf.sort(key=lambda x:x[1:])
    ans=lf+nof
    return ans

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
        #print('~')