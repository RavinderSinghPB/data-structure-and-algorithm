def reverseAlternate(Str):
    res = ''
    count = 0
    temp = ''
    for i in range(len(Str)):
        if Str[i] != ' ':
            temp += Str[i]
        if Str[i] == ' ' or i == len(Str) - 1:
            count += 1

            if count % 2 == 0:
                temp = temp[::-1]
            res += temp
            res += ' '
            temp = ''
    return res


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        Str = input()

        print(reverseAlternate(Str))
