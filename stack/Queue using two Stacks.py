# contributed by RavinderSinghPB

def qPush(x,s1,s2):
    s1.append(x)


def qPop(s1,s2):

    if not s2:
        if not s1:
            return -1

        while s1:
            r=s1.pop()
            s2.append(r)

        k=s2.pop()

        while s2:
            l=s2.pop()
            s1.append(l)

        return k

    return -1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                qPush(qtyp_qry[i + 1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(qPop(stack1, stack2), end=' ')
                i += 1

        print()

