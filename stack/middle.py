def stackMiddle(n,stack):

    while len(stack)> n-n//2:
        stack.pop()

    return stack[-1]


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        stack=[int(x) for x in input().split()]

        print(stackMiddle(n, stack))