from collections import deque


def minStep(n):
    stpcnt = 0

    qu = deque([2, 3])
    vstd = {2, 3}

    while qu:
        stpcnt += 1

        nxtqu = []
        for cn in qu:
            for an in [cn + 1, 3 * cn]:
                if an == n:
                    return stpcnt + 1

                if an > n:
                    continue
                if an not in vstd:
                    nxtqu.append(an)
        qu = nxtqu

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n=int(input())

        print(minStep(n))
