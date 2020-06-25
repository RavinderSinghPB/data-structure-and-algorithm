class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next


def Segregate(head, n):
    evn, odd = Node(0), Node(0)
    he, ho = evn, odd

    tmp = head

    while tmp:

        if tmp.data % 2 == 0:
            evn.next = Node(tmp.data)
            evn = evn.next
        else:
            odd.next = Node(tmp.data)
            odd = odd.next
        tmp = tmp.next

    return he.next, ho.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = LinkedList()
        tail = None

        for nodeData in arr:
            ll.append(nodeData)

        hEvn,hOdd=Segregate(ll.head,n)

        printList(hEvn)
        printList(hOdd)
        print()
