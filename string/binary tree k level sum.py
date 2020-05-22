def levelSum(k,a):
    l = -1
    s = 0
    i = 0
    while (i < len(a)):
        if a[i] == "(":
            l += 1
        elif a[i] == ")":
            l -= 1
        elif k == l:
            t = ""
            while (a[i] != '(' and i < len(a)):
                t += a[i]
                i += 1
            s += int(t)
            continue
        i += 1
    return s


if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        k = int(input())
        s = input()

        print(levelSum(k,s))
