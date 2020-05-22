class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0


def insertFront(front,rear,data):
    node = Node(data)
    if not front:
        return (node,node)

    node.next=front
    front.prev=node

    return (node,rear)

def insertRear(front,rear,data):
    node =Node(data)
    if not front:
        return (node,node)

    node.prev = rear
    rear.next = node

    return (front,node)


def delFront(front,rear):
    if not front:
        return (None,None)

    if front==rear:
        return (None,None)

    temp=front.next

    front.next.prev=None

    return (temp,rear)

def delRear(front,rear):
    if not front:
        return (None,None)

    if front==rear:
        return (None,None)

    temp=rear.prev

    rear.prev.next=None

    return (front,temp)


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        q=int(input())

        dq=Deque()

        for _ in range(q):

            qry=input().split()

            if qry[0]=='if':
                x=int(qry[1])
                dq.front,dq.rear=insertFront(dq.front,dq.rear,x)

            elif qry[0]=='ir':
                x=int(qry[1])
                dq.front,dq.rear=insertRear(dq.front,dq.rear,x)

            elif qry[0]=='df':
                dq.front,dq.rear=delFront(dq.front,dq.rear)

            else:
                dq.front,dq.rear=delRear(dq.front,dq.rear)


        if dq.front:
            print(dq.front.data)
            print(dq.rear.data)
        else:
            print(-1)
            print(-1)




