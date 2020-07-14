# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, tail, data):
        head = self.head

        node = Node(data)

        if not head:
            self.head = node
            self.tail = node
            return node

        tail.next = node
        node.prev = tail
        self.tail = node
        return node

    def delete(self, node):

        if not node:
            return

        if node == self.head:
            if node == self.tail:
                self.tail = self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev


def displayList(head):
    while head:
        print(head.data, end=' ')
        pvs = head
        head = head.next

    # while pvs:
    #     print(pvs.data, end=' ')
    #     pvs =  pvs.prev


def nonRepeating(arr, n):
    dct = dict()

    dll = doublyLL()
    tail = None

    for e in arr:

        if e not in dct:

            if dll.head:
                print(dll.head.data, end=' ')
            else:
                print(e, end=' ')
            tail = dll.insert(tail, e)

            dct[e] = tail

        else:
            if not dll.head or dll.head.data == e:
                print(-1, end=' ')

            else:
                print(dll.head.data, end=' ')
            node = dct[e]
            dll.delete(node)
            dct[e] = None


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        arr = input().split()

        try:
            nonRepeating(arr, n)
        except:
            print(tcs,'#############################################################################################')
