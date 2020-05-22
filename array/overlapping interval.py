def overlappedInterval(parr,n):
    parr.sort()

    fir=0

    for i in range(1,n):

        if parr[fir][1]>=parr[i][0]:
            parr[fir][1]=max(parr[fir][1],parr[i][1])
        else:
            fir+=1
            parr[fir][0]=parr[i][0]
            parr[fir][1]=parr[i][1]

    for i in range(fir,n-1):
        parr.pop()
    return parr





if __name__=='__main__':
    t= int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        parr=[]

        i=0
        while i<2*n:
            parr.append([arr[i],arr[i+1]])
            i+=2

        ans=overlappedInterval(parr,n)

        for e in ans:
            print(*e,end=' ')
        print()
        # print('~')
'''
3
4
1 3 2 4 6 8 9 10
4
6 8 1 9 2 4 4 7
6
32 37 25 13 76 83 94 52 41 12 58 28
'''