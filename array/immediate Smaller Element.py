def immediateSmall(arr,n):
    for i,e in enumerate(arr[:-1]):
        if arr[i+1]<e:
            print(arr[i+1],end=' ')
        else:
            print(-1,end=' ')
    print(-1)

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        immediateSmall(arr,n)