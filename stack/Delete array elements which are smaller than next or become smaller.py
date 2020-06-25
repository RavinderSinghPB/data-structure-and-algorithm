def deleteElements(arr, n, k):
    # create an empty stack st
    st = []
    st.append(arr[0])

    # index to mantain the top
    # of the stack
    top = 0
    count = 0

    for i in range(1, n):

        # pop till the present element
        # is greater than stack's top
        # element
        while (len(st) != 0 and count < k
               and st[top] < arr[i]):
            st.pop()
            count += 1
            top -= 1

        st.append(arr[i])
        top += 1

    for e in st:
        print(e, end=' ')


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())

        deleteElements(arr,n,k)
        print()