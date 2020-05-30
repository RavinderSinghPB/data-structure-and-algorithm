def removeAdj(arr,n):
    stk=[]
    for e in arr:
        if stk and stk[-1]==e:
            stk.pop()
        else:
            stk.append(e)
    return len(stk)

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[x for x in input().split()]

        print(removeAdj(arr,n))