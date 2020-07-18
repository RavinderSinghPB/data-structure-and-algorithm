def performOperation(n):
    s = str(n)
    mmi = mma = ''

    for i in range(len(s)):
        if s[i] == '6':
            mmi += '5'
        else:
            mmi += s[i]

    for i in range(len(s)):
        if s[i] == '5':
            mma += '6'
        else:
            mma += s[i]
    print(mmi,mma)
    return int(mmi) + int(mma)


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())

    print(performOperation(n))
