def eraseAt(deq,x):
    x
    ad=deque()

    for i in range(x):
        ad.append(deq.popleft())
    deq.popleft()

    while ad:
        deq.appendleft(ad.pop())

def eraseInRange(deq,s,e):

    ad=deque()

    for i in range(s):
        ad.append(deq.popleft())
    deq.popleft()

    for i in range(e-s):
        deq.popleft()

    while ad:
        deq.appendleft(ad.pop())

def eraseAll(deq):
    deq.clear()









if __name__ == '__main__':

    from collections import deque

    tcs= int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        qry=input().split()

        deq=deque(arr)

        if int(qry[0])==1:
            x=int(qry[1])
            eraseAt(deq,x)

        elif int(qry[0])==2:
            start,end=int(qry[1]),int(qry[2])
            eraseInRange(deq,start,end)

        else:
            eraseAll(deq)

        print(*deq)


