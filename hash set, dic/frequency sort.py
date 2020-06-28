from collections import defaultdict


def freqSort(arr, n):
    frq = defaultdict(int)

    for e in arr:
        frq[e] += 1

    ans = [(e, frq[e]) for e in arr]
    ans.sort()

    ans.sort(key=lambda x: x[1],reverse=True)

    for e in ans:
        print(e[0],end=' ')



if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]

        freqSort(arr, n)
        print()
