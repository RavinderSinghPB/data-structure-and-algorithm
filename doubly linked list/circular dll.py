# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            return node

        tail.next = node
        node.prev = tail
        return node


def displayList(head):
    h=head
    while head.next!=h:
        print(head.data, end=' ')
        pvs = head
        head = head.next
    print(head.data)

    print(head.data,end=' ')
    p=pvs
    while pvs.prev!=p:
        print(pvs.data, end=' ')
        pvs = pvs.prev
    #print(pvs.data,end=' ')


if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dll = doublyLL()

        tail = None

        for nodeData in arr:
            tail = dll.insert(tail, nodeData)

        # making circular
        tail.next = dll.head
        dll.head.prev = tail

        displayList(dll.head)
        print()



