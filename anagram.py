from collections import defaultdict as dd
def Anagrams(s,n):
    d=dd(list)

    for i,e in enumerate(s):
        e=str(sorted(e))
        d[e].append(s[i])

    res=[]
    for l in d.values():
        res.append(l)
    return res


if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        strings=input().split()
        ans=Anagrams(strings,n)
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()
