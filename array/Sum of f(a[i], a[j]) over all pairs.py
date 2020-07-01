def sumPair(a, n):
    # map to keep a count of occurrences
    cnt = dict()

    # Traverse in the list from start to end
    # number of times a[i] can be in a pair and
    # to get the difference we subtract pre_sum.
    ans = 0
    pre_sum = 0
    for i in range(n):
        ans += (i * a[i]) - pre_sum
        pre_sum += a[i]

        # if the (a[i]-1) is present then
        # subtract that value as f(a[i], a[i]-1)=0
        if (a[i] - 1) in cnt:
            ans -= cnt[a[i] - 1]

            # if the (a[i]+1) is present then add that
        # value as f(a[i], a[i]-1)=0 here we add
        # as a[i]-(a[i]-1)<0 which would have been
        # added as negative sum, so we add to remove
        # this pair from the sum value
        if (a[i] + 1) in cnt:
            ans += cnt[a[i] + 1]

            # keeping a counter for every element
        if a[i] not in cnt:
            cnt[a[i]] = 0
        cnt[a[i]] += 1

    return ans


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):

        n=int(input())
        arr = [int(x) for x in input().split()]

        print(sumPair(arr,n))