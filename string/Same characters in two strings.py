def sameChar(A, B):
    count = 0

    A = A.lower()
    B = B.lower()

    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    return count


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()

        print(sameChar(A, B))
