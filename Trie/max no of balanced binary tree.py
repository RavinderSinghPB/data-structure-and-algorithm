def cnt(h,dp):
    if h in dp:
        return dp[h]

    if h-1 in dp:
        h1=dp[h-1]
    else:
        dp[h-1]=cnt(h-1,dp)
        h1=dp[h-1]

    if h-2 in dp:
        h2=dp[h-2]
    else:
        dp[h-2]=cnt(h-2,dp)
        h2=dp[h-2]

    dp[h]= dp[h-1]*(2*dp[h-2]+dp[h-1])
    return dp[h]

def maxBBT(h):
    mod=1000000007
    dp=dict()
    dp[0]=dp[1]=1
    for i in range(2,h+1):
        dp[i]= (dp[i-1]*(2*(dp[i-2]+dp[i-1])%mod)%mod)

    return dp[h]



if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        h= int(input())

        print(maxBBT(h))