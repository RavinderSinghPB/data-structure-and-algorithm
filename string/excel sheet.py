def ExcelColumn(n):
    # To store result (Excel column name)
    s=''

    # To store current index in str which is result
    i = 0

    while n > 0:
        # Find remainder
        rem = n % 26

        # if remainder is 0, then a
        # 'Z' must be there in output
        if rem == 0:
            s+='Z'
            i += 1
            n = (n // 26) - 1
        else:
            s+=chr((rem - 1) + ord('A'))
            i += 1
            n = n // 26

    return s[::-1]


def ExcelColumnNumber(s):
    # This process is similar to binary-to-
    # decimal conversion
    result = 0;
    for B in range(len(s)):
        result *= 26;
        result += ord(s[B]) - ord('A') + 1;

    return result;

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        s=input()
        print(ExcelColumnNumber(s))
