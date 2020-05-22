from collections import deque

def CheckSub(arr,n):
    l=[]

    if len(arr)<3:
        return False
    # if len(arr)==3:
    #     if arr[0]<arr[2]<arr[1]:
    #         return True
    #     else:
    #         return False

    if arr[0] < arr[2] < arr[1]:
        return True

    minn=[0]*n

    minn[0]=arr[0]

    for i in range(n):
        minn[i]=min(minn[i-1],arr[i])

    for j in range(n-1,-1,-1):
        if arr[j]>minn[j]:
            while l and l[-1]<=minn[j]:
                l.pop()

            if l and l[-1]<arr[j]:
                return True
            l.append(arr[j])
    return False










if __name__ == '__main__':

    tcs=int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        print(CheckSub(arr,n))