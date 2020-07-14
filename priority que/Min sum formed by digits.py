import heapq as hq


def minDigitSum(arr, n):
    hq.heapify(arr)

    n1 = 0
    n2 = 0

    i=1
    while arr:

        if i%2==0:
            n1= n1*10 + hq.heappop(arr)
        else:
            n2 = n2*10 +hq.heappop(arr)

        i+=1

    return n1+n2

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]

        print(minDigitSum(arr,n))
