def sortString(s):
    arr = [0] * 26

    for e in s:
        arr[ord(e) - ord('a')] += 1

    for i, e in enumerate(arr):
        print(chr(i + ord('a')) * e, end='')



if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        S = input()

        sortString(S)
        print()
