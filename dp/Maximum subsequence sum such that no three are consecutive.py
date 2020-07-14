def maxSumThreeNonAdj(arr, n):
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    if n == 3:
        return max(arr[1] + arr[2], arr[0] + arr[2], arr[0] + arr[2])
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[1] + arr[2], arr[0] + arr[1], arr[0] + arr[2])

    for i in range(3, n):
        dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3], dp[i - 1])

    return dp[n - 1]


# need corrections
# def maxSumThreeNonAdj(arr, n):
#     if n == 1:
#         return arr[0]
#     if n == 2:
#         return arr[0] + arr[1]
#     if n == 3:
#         return max(arr[1] + arr[2], arr[0] + arr[2], arr[0] + arr[2])
#
#     mi=arr[0]
#     mi1 = arr[0]+arr[1]
#     mi2 = max(arr[1]+arr[2],arr[0]+arr[1],arr[0]+arr[2])
#
#     for i in range(3,n):
#         temp2=mi
#         mi=max(arr[i]+mi1,arr[i]+arr[i-1]+mi,mi2)
#         mi2 = temp2


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = [int(x) for x in input().split(', ')]

        print(maxSumThreeNonAdj(arr, n))
