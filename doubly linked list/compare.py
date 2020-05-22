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

def compareCLL(head1,head2):
    h1,h2=head1,head2

    while h1 and h2 and h1.next!=head1 and h2.next!=head2:

        if h1.data!=h2.data:
            return 0
        h1=h1.next
        h2=h2.next

    if h1 and not h2:
        return 0
    elif not h2 and h1:
        return 0
    elif h1.next==head1 and h2.next!=head2:
        return 0
    elif h1.next!=head1 and h2.next==head2:
        return 0
    return 1



if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        n2=int(input())
        arr2=[int(x) for x in input().split()]

        dll1=doublyLL()
        tail=None
        for nodeData in arr1:
            tail=dll1.insert(tail,nodeData)

        # making circular
        tail.next = dll1.head
        dll1.head.prev = tail

        dll2 = doublyLL()
        tail = None
        for nodeData in arr2:
            tail = dll2.insert(tail, nodeData)

        # making circular
        tail.next = dll2.head
        dll2.head.prev = tail

        print(compareCLL(dll1.head,dll2.head))



