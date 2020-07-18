def reverseString(S):
    hsmp = [0] * 26

    ans = ''

    for i in range(len(S) - 1, 0, -1):

        if S[i] != ' ' and not hsmp[ord(S[i]) - ord('A')]:
            ans += S[i]
            hsmp[ord(S[i]) - ord('A')] = 1

    return ans


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        S = input()

        print(reverseString(S))
