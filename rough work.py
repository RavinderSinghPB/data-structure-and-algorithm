def lcs(s1,s2,m,n,mz):

    pass

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n,m=[int(x) for x in input().split()]
        s1=input()
        s2=input()

        mz=[[-1]*(n+1)]*(m+1)

        print(lcs(s1,s2,m,n,mz))