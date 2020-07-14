def maxsum(arr, n):
    m = [0] * n
    maxsum = 0

    if arr[0] > 0:
        m[0] = arr[0]
    else:
        m[0] = 0

    for i in range(n):
        if m[i - 1] + arr[i] > 0:
            m[i] = m[i - 1] + arr[i]
        else:
            m[i] = 0

    for i in range(n):
        if m[i] > maxsum:
            maxsum = m[i]
    return maxsum


arr = [int(x) for x in input().split(', ')]
print(maxsum(arr, len(arr)))
