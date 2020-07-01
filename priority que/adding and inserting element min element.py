'''
Given an array arr[] and an integer K, you have to Add first two minimum elements of the array until all the elements are greater than K and find the number of such operations required.

Examples:

Input : arr[] = {1 10 12 9 2 3}
          K = 6
Output : 2
First we add (1 + 2), now the new list becomes
3 10 12 9 3, then we add (3 + 3),  now the new
list becomes 6 10 12 9, Now all the elements in
the list are greater than 6. Hence the output is
2 i:e 2 operations are required
to do this.
'''

import heapq as hq


def noOfOprtn(arr, n, k):

    hq.heapify(arr)

    ans = 0


    while arr:
        ele1 = hq.heappop(arr)


        if ele1 >= k:
            return ans

        if arr:
            ele2 = hq.heappop(arr)
        else:
            return -1

        ans+=1

        hq.heappush(arr,ele1+ele2)
    return ans



if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n, k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        print(noOfOprtn(arr,n,k))