def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2;
    while i:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;

        if f2 % k == 0:
            return n * i

        i += 1

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        a=int(input())

        print(findPosition(a,n))