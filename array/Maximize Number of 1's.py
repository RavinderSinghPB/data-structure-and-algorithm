def maximumOnes(arr,n,m):
    r=l=c0=best=0

    while r<n:
        if c0<=m:
            if arr[r]==0:
                c0+=1
            r+=1
        if c0>m:
            if arr[l]==0:
                c0 -=1
            l+=1
        if r-l>best:
            best=r-l

    return best

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        m=int(input())

        print(maximumOnes(arr,n,m))