def inPlace(root):
    inplace(root, root)
    return root

def inplace(head,tail):

    if tail.next:
        next_head=inplace(head,tail.next)
    else:
        tmp=head.next
        head.next=tail
        tail.next=tmp
        return tmp

    if not next_head:
        return
    elif next_head==tail or next_head.next==tail:
        tail.next=None
        return None


    tmp=next_head.next
    next_head.next=tail
    tail.next=tmp
    return tmp


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    tmp = head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


'''
2
4
1 2 3 4
5
1 2 3 4 5
'''

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = inPlace(ll.head)
        printList(res)