def maxHeight(h, w, l, n):
    box = []  # arr for max box with different orientation

    for i in range(n):
        box.append((l[i] * w[i], h[i], l[i], w[i]))
        box.append((w[i] * h[i], l[i], w[i], h[i]))
        box.append((h[i] * l[i], w[i], h[i], l[i]))

    box.sort(reverse=True)

    dp = [0] * (3 * n + 1)

    mx = 0
    i = 0
    for i in range(0, (3 * n)):
        dp[i] = box[i][1]
        for j in range(0, i + 1):

            if box[i][2] < box[j][2] and box[i][3] < box[j][3]:
                mx = dp[i] = max(dp[j] + box[i][1], dp[i])

    return mx


# def maxHeight(h,w,l,n):
#     box = [] # arr for max box with different orientation
#
#     for i in range(n):
#         box.append((l[i]*w[i],h[i],l[i],w[i]))
#         box.append((w[i]*h[i],l[i],w[i],h[i]))
#         box.append((h[i]*l[i],w[i],h[i],l[i]))
#
#     box.sort(reverse=True)
#
#     dp = [0]*(3*n+1)
#
#     mx=0
#     i=0
#     for i in range(1,(3*n+1)):
#
#         for j in range(1,i):
#
#             if box[i-1][2]<box[j-1][2] and box[i-1][3]<box[j-1][3]:
#                 mx=dp[i]= max(dp[j]+box[i-1][1],dp[i])
#     return max(dp)


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N = int(input())

        arr = [int(x) for x in input().split()]
        h, w, l = [], [], []
        for i in range(0, 3 * N, 3):
            h.append(arr[i])
            w.append(arr[i + 1])
            l.append(arr[i + 2])

        print(maxHeight(h, w, l, N))
