def orderString(s):
    min_i = 0
    max_i = 0

    for i in range(1, len(s)):
        if s[min_i] > s[i]:
            min_i = i
        elif s[max_i] < s[i]:
            max_i = i

    return s[min_i], s[max_i]


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n=int(input())
        s = input().split()

        print(*orderString(s))
