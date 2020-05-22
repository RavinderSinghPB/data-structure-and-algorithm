def InsertInStack(n,arr):
    stack=[]

    for e in arr:
        stack.append(e)

    return stack


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        stack=InsertInStack(n,arr)

        while stack:
            print(stack.pop(),end=' ')
