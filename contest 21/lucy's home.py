def getMax(arr,n):

    return max(arr)


def getSum(arr,n):
    return sum(arr)


def numOfPaint(arr,n,maxLen):
    ttl,numOfPaintr=0,1

    for i in range(n):
        ttl+=arr[i]

        if ttl>maxLen:
            ttl=arr[i]
            numOfPaintr+=1

    return numOfPaintr


def Min_Time(arr,n,k):
    lo=max(arr)
    hi=sum(arr)

    while lo<hi:
        mid=lo+(hi-lo)//2

        reqPaint=numOfPaint(arr,n,mid)

        if reqPaint<=k:
            hi=mid

        else:
            lo=mid+1

    return lo



if __name__ == '__main__':
    from math import inf

    tcs=int(input())

    for _ in range(tcs):

        k,n=[int(x) for x in input().split()]

        arr=[int(x) for x in input().split()]

        print(Min_Time(arr,n,k))