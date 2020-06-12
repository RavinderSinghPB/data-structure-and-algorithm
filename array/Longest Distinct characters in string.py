def longestUniqueSubstr(string):
    # Initialize the last index array as -1,
    lastIndex = [-1] * 256

    n = len(string)
    res = 0  # Result

    # Initialize start of current window
    i = 0

    # Move end of current window
    for j in range(0, n):
        # Find the last index of str[j]
        # Update i (starting index of current window)
        # as maximum of current value of i and last
        # index plus 1
        i = max(i, lastIndex[ord(string[j])] + 1)

        # Update result if we get a larger window
        res = max(res, j - i + 1)

        # Update last index of j.
        lastIndex[ord(string[j])] = j

    return res

if __name__ == '__main__':
    T=int(input())

    for _ in range(T):

        s=input()
        print(longestUniqueSubstr(s))