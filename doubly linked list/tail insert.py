#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def displayList(head):
    while head:
        print(head.data,end=' ')
        pvs=head
        head=head.next
    print()

    while pvs:
        print(pvs.data,end=' ')
        pvs=pvs.prev

def insertInhead(head,data):
    node=Node(data)
    if not head:
        return node

    head.prev=node
    node.next=head
    return node

def insertInTail(head,data):
    h=head

    while h:
        pvs=h
        h=h.next

    node=Node(data)
    pvs.next=node
    node.prev=pvs
    return head

def sortedInsert(head,data):

    while head and head.data<data:
        pvs=head
        head=head.next

    node=Node(data)
    node.next=head
    node.prev=pvs
    pvs.next=node





if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        Data=int(input())

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        dll.head=sortedInsert(dll.head,Data)
        displayList(dll.head)
        print()



