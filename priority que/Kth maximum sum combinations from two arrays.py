""" Read
Given two equally sized arrays (A, B) and N (size of both arrays).
A sum combination is made by adding one element from array A and another element of array B.
Display the maximum K valid sum combinations from all the possible sum combinations.
"""

import heapq as hq


def solve(N, K, A, B):
    A.sort()
    B.sort()

    max_hp = []
    myset = set()

    hq.heappush(max_hp, ((-(A[N - 1] + B[N - 1]),
                          (N - 1, N - 1))))

    myset.add((N - 1, N - 1))

    for count in range(K):
        sum_idx = hq.heappop(max_hp)

        if count == K - 1:
            return -sum_idx[0]

        i, j = sum_idx[1][0], sum_idx[1][1]

        sum = A[i - 1] + B[j]

        if (i - 1, j) not in myset:
            hq.heappush(max_hp, (-sum, (i - 1, j)))
            myset.add((i - 1, j))

        sum = A[i] + B[j - 1]

        if (i, j - 1) not in myset:
            hq.heappush(max_hp, (-sum, (i, j - 1)))
            myset.add((i, j - 1))
    return -1


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, K = [int(x) for x in input().split()]
        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]

        print(solve(N, K, A, B))
