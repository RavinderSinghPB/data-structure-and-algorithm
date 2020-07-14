class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return self.a, self.b


def maxChainLen(arr, n):
    max = 0

    # Initialize MCL(max chain length) values for all indices
    mcl = [1 for i in range(n)]

    arr.sort(key=lambda x: (x.a, x.b))

    # Compute optimized chain length values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i].a > arr[j].b and mcl[i] < mcl[j] + 1:
                mcl[i] = mcl[j] + 1

    # mcl[i] now stores the maximum
    # chain length ending with pair i

    # Pick maximum of all MCL values
    for i in range(n):
        if max < mcl[i]:
            max = mcl[i]

    return max


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        arr = [int(x) for x in input().split()]

        Parr = []

        i = 0
        while n * 2 > i:
            Parr.append(Pair(arr[i], arr[i + 1]))

            i += 2

        # print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
