from collections import defaultdict


def countWords(List, n):
    map = defaultdict(int)

    for e in List:
        map[e] += 1

    count = 0
    for k, v in map.items():
        print(k,v)
        if v == 2:
            count += 1
    return count


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()

        print(countWords(List, n))
