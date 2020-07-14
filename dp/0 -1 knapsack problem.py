def knapsack(cpct, wt, val, n):
    if n == 0 or cpct == 0:
        return 0
    row = n + 1
    colmn = cpct + 1

    dp = [[0 for i in range(colmn)] for j in range(row)]

    for i in range(1, row):
        for j in range(1, colmn):
            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
    return dp[n][colmn - 1]


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N = int(input())
        W = int(input())
        val = [int(x) for x in input().split()]
        wt = [int(x) for x in input().split()]

        print(knapsack(W, wt, val, N))
