def editDistance(str1, str2, n1, n2):
    dp = [[0 for i in range(n1 + 1)] for j in range(2)]

    for i in range(n1 + 1):
        dp[0][i] = i

    for i in range(1, n2 + 1):

        for j in range(0, n1 + 1):

            if j == 0:
                dp[i % 2][j] = i

            elif str1[j - 1] == str2[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = 1 + min(dp[(i - 1) % 2][j],
                                       min(dp[i % 2][j - 1],
                                           dp[(i - 1) % 2][j - 1]))

    return dp[n2 % 2][n1]


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n1, n2 = [int(x) for x in input().split()]

        str1, str2 = input().split()

        print(editDistance(str1, str2, n1, n2))
