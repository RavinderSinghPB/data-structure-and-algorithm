def uniqueEle(arr,n,k):
    ele = [0]*1000001

    for e in arr:
        ele[e]+=1

    for i,e in enumerate(ele[1:]):
        if e==1:
            return i+1


if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        n,k=[int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        print(uniqueEle(arr,n,k))