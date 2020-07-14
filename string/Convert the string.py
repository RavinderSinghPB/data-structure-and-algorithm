def transform(Str):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    res = ''
    for e in Str:
        if e in vowels:
            continue
        else:
            if ord(e) < ord('Z'):
                char = chr(ord(e) + 32)
            else:
                char = chr(ord(e) - 32)
        res += '#' + char

    return res


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        Str = input()

        print(transform(Str))
