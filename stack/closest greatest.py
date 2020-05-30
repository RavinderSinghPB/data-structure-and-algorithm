def closestGreatest(arr,n):
    stk=[]
    sm=0

    for i,e in enumerate(arr):
        while stk and stk[-1]<e:
            #print(i,e,stk)
            #print(e,end=' ')
            #print(e,sm)
            sm+=e
            stk.pop()
        stk.append(e)
    return sm

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        print(closestGreatest(arr,n))