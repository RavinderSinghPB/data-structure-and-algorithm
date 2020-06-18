# def lcs(s1,s2,m,n):
#
#     if m==-1 or n==-1:
#         return 0
#
#     elcs=0
#     if s1[m]==s2[n]:
#         elcs=1+lcs(s1,s2,m-1,n-1)
#
#     s1lcs=lcs(s1,s2,m,n-1)
#     s2lcs=lcs(s1,s2,m-1,n)
#
#     return max(elcs,s1lcs,s2lcs)

# tabulation
def lcsTabu(s1, s2, n1, n2):
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]

    for i in range(1, n1 + 1):

        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n1][n2]


def lcs(s1, s2, m, n, mz):
    if mz[m][n]:
        return mz[m][n]

    if m == -1 or n == -1:
        mz[m][n] = 0
        return 0

    if s1[m] == s2[n]:
        if mz[m - 1][n - 1]:
            mz[m][n] = 1 + mz[m - 1][n - 1]
        else:
            mz[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, mz)

        return mz[m][n]

    else:
        if mz[m][n - 1]:
            s1lcs = mz[m][n - 1]
        else:
            s1lcs = mz[m][n - 1] = lcs(s1, s2, m, n - 1, mz)
        if mz[m - 1][n]:
            s2lcs = mz[m - 1][n]
        else:
            s2lcs = mz[m - 1][n] = lcs(s1, s2, m - 1, n, mz)

        return max(s1lcs, s2lcs)


def lcsu(s1, s2, m, n, mz):
    if m == 0 or n == 0:
        return 0

    if mz[m][n] != -1:
        return mz[m][n]

    if s1[m - 1] == s2[n - 1]:
        mz[m][n] = 1 + lcsu(s1, s2, m - 1, n - 1, mz)
        return mz[m][n]
    else:
        mz[m][n] = max(lcsu(s1, s2, m - 1, n, mz), lcsu(s1, s2, m, n - 1, mz))
        return mz[m][n]


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n, m = [int(x) for x in input().split()]
        s1 = input()
        s2 = input()

        mz = [[-1] * (n + 1)] * (m + 1)

        print(lcs(s1, s2, m, n, mz))
