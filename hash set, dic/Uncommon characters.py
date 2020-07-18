def UncommonChars(A, B):
    res = ''

    present = [0] * 26

    for e in A:
        present[ord(e) - ord('a')] = 1

    for e in B:
        if present[ord(e) - ord('a')] == 1 or present[ord(e) - ord('a')] ==-1:
            present[ord(e) - ord('a')] = -1  # 2 means present in both
        else:
            present[ord(e) - ord('a')] = 2

    res = ''

    for i, e in enumerate(present):
        if e == 1 or e==2:
            res += chr(i + ord('a'))

    return res


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()

        print(UncommonChars(A, B))
