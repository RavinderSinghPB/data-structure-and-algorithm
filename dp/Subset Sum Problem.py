def subsetSum(arr, n):
    sm = sum(arr)
    if n == 0 or sm % 2 != 0:
        print('NO')
        return

    sm = sm // 2

    dp = [[0 for i in range(sm + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, sm + 1):

            if j == arr[i - 1]:
                dp[i][j] = j

            elif j > arr[i - 1] and dp[i - 1][j - arr[i - 1]]:
                dp[i][j] = j
            else:
                dp[i][j] = dp[i - 1][j]

    for e in dp:
        print(*e)
    if dp[n][sm]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())

        arr = [int(x) for x in input().split()]
        subsetSum(arr, n)
