from math import inf

# need improvment

def minCoin(coins, N, val):
    coins.sort()
    dp = [inf] * (val + 1)
    dp[0] = 0

    for i in range(1, val + 1):

        for e in coins:
            if e <= i:
                if dp[i-e]!= inf:
                    dp[i]= min(dp[i],dp[i-e]+1)
            else:
                break
    return dp[val]


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        val = int(input())
        N = int(input())
        coins = [int(x) for x in input().split()]

        print(minCoin(coins, N, val))
