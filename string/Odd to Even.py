def makeEven(Str):
    n=len(Str)
    mei = -1
    for i, e in enumerate(Str):
        if int(e) % 2 == 0 and int(e) < int(Str[-1]):
            mei = i
            break
        elif int(e) % 2 == 0:
            mei = i

    if mei == -1:
        return Str
    #print(mei,Str[:mei],Str[-1],Str[mei])
    ans = Str[:mei] + Str[-1] + Str[mei+1:n-1]+Str[mei]
    return ans


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        Str = input()
        print(makeEven(Str))
