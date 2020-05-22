def factorial(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


# to print range of length n
# having all composite integers
def Range(n):
    a = factorial(n + 2) + 2
    b = a + n - 1

    if n==(b-a+1):
        return 1
    else:
        return 0

    #print("[" + str(a) + ", " + str(b) + "]")



if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())

        print(Range(n))