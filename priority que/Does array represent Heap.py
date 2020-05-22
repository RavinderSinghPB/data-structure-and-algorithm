def arrayRepresentHeap(arr,n):
    flag=1

    for i in range(n//2-1):
        if (arr[i]<arr[(2*i)+1]) or (arr[i]<arr[(2*i)+2]):
            flag=0
            break
    if flag ==0:
        return 0
    else:
        return 1




if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        print(arrayRepresentHeap(arr,n))