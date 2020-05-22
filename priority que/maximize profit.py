import heapq as hq


def maxProfit(s,k,n):
    s=[-x for x in s]
    hq.heapify(s)

    p=0
    c=0

    while c<n:
        top=-1*hq.heappop(s)

        if top==0:
            break

        p+=top

        top-=1
        hq.heappush(s,-top)

        c+=1

    return p




if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        k,n=[int(x) for x in input().split()]
        seats=[int(x) for x in input().split()]

        print(maxProfit(seats,k,n))