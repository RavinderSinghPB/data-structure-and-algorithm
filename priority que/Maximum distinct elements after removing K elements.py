import heapq as hq
from collections import defaultdict


def maxDistinctEle(arr, n, k):
    frqDct = defaultdict(int)  # to store elem and its freq

    for e in arr:
        frqDct[e] += 1

    frq = list(frqDct.values())  # frequency list

    hq.heapify(frq)

    ans = 0
    unq = 0
    while k > 0 and frq:

        eleFrq = hq.heappop(frq)

        if eleFrq == 1:
            unq += 1
            continue

        removedElem = eleFrq - 1

        if removedElem <= k:
            k = k - removedElem
            ans += 1
        else:
            k=0
            break

    if k:
        if unq >= k:
            unq = unq - k

    return ans + unq


# def maxDistinctEle(arr, n, k):
#     frqDct = defaultdict(int)   # to store elem and its freq
#
#     for e in arr:
#         frqDct[e] += 1
#
#     frq = list(frqDct.values())   # frequency list
#     print(frq)
#
#     hq.heapify(frq)
#
#     ans=0
#     while k>0 and frq:
#
#         eleFrq = hq.heappop(frq)
#
#         removedElem = eleFrq - 1
#
#         if removedElem<=k:
#             k=k-removedElem
#             ans+=1
#
#         print(k,eleFrq,removedElem,frq)
#
#     return ans


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n, k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        print(maxDistinctEle(arr, n, k))
        print('~')
