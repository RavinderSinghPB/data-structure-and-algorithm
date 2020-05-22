def GCD(a, b):
    while a != b and min(a, b) != 0:
        if a > b:
            a -= b
        else:
            b = b - a

    return a


def smallestSubArray(arr,g,n):
    k = 0
    for i in range(n-1):
        if GCD(arr[i], arr[i + 1]) == g:
            k = 1
            break

    if k == 0:
        print(-1)
    else:
        print(2)

if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        g=int(input())
        n = int(input())
        arr = [int(x) for x in input().split()]

        smallestSubArray(arr,g, n)


