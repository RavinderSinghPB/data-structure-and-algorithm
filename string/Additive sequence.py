from collections import deque
def isValid(num):
    if len(num)>1 and num[0]=='0':
        return False
    return True

def val(a,pos):
    if pos>=len(a) or pos<0:
        return 0
    #print(a,pos)
    return int(a[pos])


def addString(a,b):
    sm=''
    i=len(a)-1
    j=len(b)-1
    carry=0

    while i>=0 or j>=0:
        t=val(a,i)+val(b,j)+carry
        sm+=str(t%10)
        carry=t//10
        i-=1
        j-=1

    if carry:
        sm+=str(carry)
    sm=sm[::-1]
    return sm

def checkAddition(res,a,b,c):
    if not isValid(a) or not isValid(b):
        return False

    sm=addString(a,b)

    if sm==c:
        res.append(sm)
        return True

    if len(c)<=len(sm) or sm!=c[0:len(sm)]:
        return False

    else:
        res.append(sm)

        return checkAddition(res,b,sm,c[0:len(sm)])

def additiveSequence(num):
    res=deque()
    l=len(num)

    for i in range(1,l//2+1):
        for j in range(1,(l-i)//2+1):
            if checkAddition(res,num[0:i],num[i:i+j],num[i+j:]):
                res.appendleft(num[i:i+j])
                res.appendleft(num[:i])
                return res
    return res

def isAdditiveSequence(n):
    res=additiveSequence(n)
    #print(*res)
    if res:
        return 1
    else:
        return 0



# def isAdditiveSequence(s):
#
#     if len(s)==1 or len(s)==2:
#         return 1
#
#     pv=int(s[0])+int(s[1])
#     i=2
#     while i<=len(s):
#         lpv=len(str(pv))
#
#         if i+lpv++1>=len(s):
#             return 0
#
#         cn=s[i:i+lpv+1]
#
#         if pv!=int(cn):
#             return 0
#         else:
#             pv=pv+int(cn)
#             i+=len(cn)+1
#     return 1


if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        s=input()

        print(isAdditiveSequence(s))