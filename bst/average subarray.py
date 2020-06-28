def findInd(presum,n,val):
    l=0
    h=n-1

    ans = -1

    while l<=h:
        mid=(l+h)//2

        if presum[mid][0]<=val:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans

def LongestSub(arr,n,x):

    for i in range(n):
        arr[i]-=x

    maxLen=0

    presum=[]
    sm=0

    minInd=[inf]*n

    for i in range(n):
        sm=sm+arr[i]
        presum.append((sm,i))

    presum.sort()

    minInd[0]=presum[0][1]

    for i in range(n):
        minInd[i]=min(minInd[i-1],presum[i][1])

    sm=0

    for i in range(n):
        sm=sm+arr[i]

        if sm>=0:
            maxLen=i+1

        else:
            ind=findInd(presum,n,sm)

            if ind!=-1 and minInd[ind]<i:
                maxLen=max(maxLen,i-minInd[ind])
    return maxLen

if __name__ =='__main__':
    from mathpro.math import inf
    tcs=int(input())

    for _ in range(tcs):
        N,X=[int(e) for e in input().split()]
        arr=[int(e) for e in input().split()]

        print(LongestSub(arr,N,X))