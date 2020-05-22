# def deque_Init(arr,n):
#     dq=deque(arr)
#     return dq
#
#
# if __name__ == '__main__':
#
#     from collections import deque
#
#     tcs= int(input())
#
#     for _ in range(tcs):
#         n=int(input())
#         arr=[int(x) for x in input().split()]
#
#         dq=deque_Init(arr,n)
#
#         for e in dq:
#             print(e,end=' ')
#         print()
#

def printDeque(deq):
    for e in deq:
        print(e,end=' ')

if __name__ == '__main__':

    from collections import deque

    tcs= int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]

        deq=deque(arr)

        printDeque(deq)
        print()