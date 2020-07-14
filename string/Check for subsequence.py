def isSubSequence(A, B):
    i = j = 0

    while i < len(B) and j < len(A):
        if A[j] == B[i]:
            j += 1

    return j == len(A)


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A = input()
        B = input()

        if isSubSequence(A < B):
            print(1)
        else:
            print(0)
