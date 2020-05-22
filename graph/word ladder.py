import collections

import collections


def WordLadderLength(bw, ew, wl):
    if ew not in wl:
        return 0
    if bw in wl:
        wl.remove(bw)

    if bw==ew:
        return 2


    lvl, wlnt = 0, len(bw)

    qu = collections.deque()
    qs=collections.deque()

    qu.append(bw)
    qs.append(1)


    while qu:

        word=qu.popleft()
        stp=qs.popleft()

        if word==ew:
            return stp

        orig_c=list(word)

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                tmp=word[i]
                if word[i]!=c:
                    next_word = word[:i] + c + word[i + 1:]
                else:
                    continue

                if next_word in wl:
                    qu.append(next_word)
                    qs.append(stp+1)

                    wl.remove(next_word)
    return 0


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())

        dic = set()
        for _ in range(n):
            word = input()
            dic.add(word)

        start = input()
        target = input()

        print(WordLadderLength(start, target, dic))
        # print(list(dic))
        print('~')


# def WordLadderLength(beginWord, endWord, wordList):
#     # wordList.add(endWord)
#     queue = collections.deque([[beginWord, 1]])
#     if beginWord in wordList:
#         wordList.remove(beginWord)
#     while queue:
#         word, length = queue.popleft()
#         if word == endWord:
#             return length
#         for i in range(len(word)):
#             for c in 'abcdefghijklmnopqrstuvwxyz':
#                 next_word = word[:i] + c + word[i + 1:]
#                 if next_word in wordList:
#                     wordList.remove(next_word)
#                     queue.append([next_word, length + 1])
#     return 0
#
#
# if __name__ == '__main__':
#     tcs = int(input())
#
#     for _ in range(tcs):
#         n = int(input())
#
#         dic = set()
#         for _ in range(n):
#             word = input()
#             dic.add(word)
#
#         start = input()
#         target = input()
#
#         print(WordLadderLength(start, target, dic))
#         print(list(dic))
#         print('~')




