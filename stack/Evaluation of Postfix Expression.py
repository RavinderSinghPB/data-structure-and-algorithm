def evalPostfix(exp):
    opr=['+','-','*','/',]

    stk=[]
    for e in exp:
        if e in opr:
            if e=='+':
                op1=int(stk.pop())
                op2=int(stk.pop())

                stk.append(op1+op2)
            elif e=='-':
                op1=int(stk.pop())
                op2=int(stk.pop())
                stk.append(op2-op1)
            elif e=='*':
                op1=int(stk.pop())
                op2=int(stk.pop())
                stk.append(op1*op2)
            else:
                op1=int(stk.pop())
                op2=int(stk.pop())
                stk.append(op2//op1)
        else:
            stk.append(e)
    return stk[0]

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        exp=input()

        print(evalPostfix(exp))

