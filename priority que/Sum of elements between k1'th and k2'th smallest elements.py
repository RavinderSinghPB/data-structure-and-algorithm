import heapq as hq


def sumBw(arr, n, k1, k2):
    hq.heapify(arr)

    ans=0

    for _ in range(k1):
        hq.heappop(arr)

    i=0

    while i<(k2-k1-1) and i+k1<n-1:
        ans+=hq.heappop(arr)
        i+=1


    return ans


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k1k2=input().split()
        k1,k2 = int(k1k2[0]),int(k1k2[1])

        print(sumBw(arr, n, k1, k2))
