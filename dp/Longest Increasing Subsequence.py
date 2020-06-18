def longestSubsequence(arr,n):
    dp=[0]*n

    for i,e in enumerate( arr ):

        for j in range(0,i):
            if arr[j]<e:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)+1

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]

        print(longestSubsequence(arr,N))

'''
1
9
10 22 9 33 21 50 41 60 80
'''