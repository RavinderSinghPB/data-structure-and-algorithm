def addTwoLists(first, second):
    res = prev = temp = None
    carry = sm = 0
    while first or second:
        sm = carry + (first.data if first else 0) + (second.data if second else 0)
        carry = (1 if sm >= 10 else 0)

        sm = sm % 10
        temp = Node(sm)

        if not res:
            res = temp
        else:
            prev.next = temp

        prev = temp

        if first:
            first = first.next
        if second:
            second = second.next
    if carry > 0:
        temp.next = Node(carry)
    return res


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


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n_a = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1]  # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b = int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list

        result_head = addTwoLists(a.head, b.head)
        printList(result_head)
