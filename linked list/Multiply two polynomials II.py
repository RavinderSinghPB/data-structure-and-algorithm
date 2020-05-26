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


def proOfPolynomials(head1,head2,n1,n2):

    if n2<n1:
        n1,n2=n2,n1
        head1,head2=head2,head1

    l=Llist()
    tail= None

    maxPwr=(n1-1)+(n2-1)

    i=0
    while i<=maxPwr:
        tail = l.insert(0, tail)
        i+=1
    head=l.head

    if n1<=n2:
        tmph2 = head2
        tmph=   head
        while head1:

            while tmph2:

                tmph.data+=head1.data*tmph2.data
                tmph2=tmph2.next
                tmph= tmph.next
            head1=head1.next
            head=head.next
            tmph= head
            tmph2=head2


    return l.head


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

        n1,n2 =[int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        arr2 = [int(x) for x in input().split()]

        ll1 = Llist()
        tail= None

        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)


        ll2= Llist()
        tail= None

        for nodeData in arr2:
            tail = ll2.insert(nodeData, tail)

        resHead =proOfPolynomials(ll1.head,ll2.head,n1,n2)
        printList(resHead)
