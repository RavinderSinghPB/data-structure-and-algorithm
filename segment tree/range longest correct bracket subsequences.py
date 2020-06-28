from mathpro.math import ceil, log2


class node:

    def __init__(self):
        self.op = 0  # open
        self.cl = 0  # close
        self.ttl = 0


def constSt(string, n):
    x = (int)(ceil(log2(n)))
    max_size = 2 * (int)(2 ** x) - 1

    st = [node() for _ in range(max_size)]

    constStUtl(string, st, 0, n - 1, 0)
    return st


def constStUtl(s, st, ss, se, si):
    if ss == se:

        if s[ss] == '(':
            st[si].op = 1
        else:
            st[si].cl = 1
        # print(ss,se)
        return

    mid = ss + (se - ss) // 2

    constStUtl(s, st, ss, mid, si * 2 + 1)
    constStUtl(s, st, mid + 1, se, si * 2 + 2)

    st[si].op = st[si * 2 + 1].op + st[si * 2 + 2].op - min(st[si * 2 + 1].op, st[si * 2 + 2].cl)
    st[si].cl = st[si * 2 + 1].cl + st[si * 2 + 2].cl - min(st[si * 2 + 1].op, st[si * 2 + 2].cl)
    st[si].ttl = min(st[si * 2 + 1].op, st[si * 2 + 2].cl) + st[si * 2 + 1].ttl + st[si * 2 + 2].ttl
    # print(ss,se,st[si].ttl,st[si].op,st[si].cl)


def getLongestSequence(st, n, qs, qe):
    n = gls(st, n, qs, qe, 0, n - 1, 0)
    print(2 * n.ttl)


def gls(st, n, qs, qe, ss, se, si):
    if ss >= qs and se <= qe:
        return st[si]

    if ss > qe or se < qs:
        return node()

    mid = ss + (se - ss) // 2
    l = gls(st, n, qs, qe, ss, mid, si * 2 + 1)
    r = gls(st, n, qs, qe, mid + 1, se, si * 2 + 2)
    # st[si].ttl=(st[si*2+1].op if st[si*2+2].cl>=st[si*2+1].op else st[si*2+2].cl)+st[si*2+1].ttl+st[si*2+2].ttl
    n = node()

    n.op = l.op + r.op - min(l.op, r.cl)
    n.cl = l.cl + r.cl - min(l.op, r.cl)
    n.ttl = l.ttl + r.ttl + min(l.op, r.cl)

    return n


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        string, qry = input().split()
        qry = int(qry)

        st = constSt(string, len(string))
        for q in range(qry):
            li, ri = [int(x) for x in input().split()]
            getLongestSequence(st, len(string), li, ri)
