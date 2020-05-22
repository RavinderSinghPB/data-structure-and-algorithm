def left_Rotate_Deq_ByK(deq,k):
    deq.rotate(-k)


def right_Rotate_Deq_ByK(deq,k):
    deq.rotate(k)


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        from collections import deque

        n=int(input())
        arr=[int(x) for x in input().split()]
        rTyp,k=[int(x) for x in input().split()]

        deq=deque(arr)

        if rTyp==2:
            left_Rotate_Deq_ByK(deq,k)
        else:
            right_Rotate_Deq_ByK(deq,k)

        print(*deq)