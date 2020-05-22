from math import log10

# epsilon value to maintain precision
EPS = 1e-9


def productExceptSelf(arr, n):
    # Base case
    if n == 1:
        print(0)
        return

    i, temp = 1, 1

    # Allocate memory for the product array
    prod = [1 for i in range(n)]

    # Initialize the product array as 1

    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

        # Initialize temp to 1 for product on right side
    temp = 1

    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

        # Print the constructed prod array
    # for i in range(n):
    #     print(prod[i], end=" ")

    return prod



if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=productExceptSelf(arr,n)
        print(*ans)