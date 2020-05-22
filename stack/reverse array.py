def reverseArray(n,arr):
    stack=[]

    for e in arr:
        stack.append(e)

    i=0
    while stack:

        arr[i]=stack.pop()
        i+=1



if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        reverseArray(n, arr)

        for e in arr:
            print(e,end=' ')
        print()