class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.random=None

    def __str__(self):
        return str(self.data)

def printInord(a,b):
    if (not a and not b) or (not a.random and not b.random):
        return 1
    if a.random.data==b.random.data and printInord(a.left,b.left) and printInord(a.right,b.right):
        return 1
    return False

def pInord(root):
    if not root:
        return
    pInord(root.left)
    print(root.data)
    if root.random:
        print(root.random.data,'rnd')
    pInord(root.right)


def copyLeftRightNode(node,mymap):
    if not node:
        return None
    cloneNode=Node(node.data)
    mymap[node]=cloneNode
    cloneNode.left=copyLeftRightNode(node.left,mymap)
    cloneNode.right=copyLeftRightNode(node.right,mymap)
    return cloneNode

def copyRandom(node,cloneNode,mymap):
    if not cloneNode:
        return

    cloneNode.random=mymap[node.random]
    copyRandom(node.left,cloneNode.left,mymap)
    copyRandom(node.right,cloneNode.right,mymap)

def cloneTree(node):
    if not node:
        return None
    mymap=dict()
    mymap[None]=None
    newTree=copyLeftRightNode(node,mymap)
    #print(*mymap)
    #print(*mymap.values())
    #pInord(newTree)
    copyRandom(newTree,node,mymap)

    return newTree


if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        map=dict()

        n=int(input())
        arrnode=[x for x in input().split()]

        # parent,child,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

        root=None
        i=0
        while i<3*n:

            n1,n2,lr=int(arrnode[i]),int(arrnode[i+1]),arrnode[i+2]

            if n1 in map:
                parent=map[n1]
            else:
                parent = Node(n1)
                map[n1] = parent

                if not root:
                    root = parent


            child=Node(n2)
            map[n2]=child

            if lr=='R':
                parent.right=child

            elif lr=='L':
                parent.left=child

            else:
                parent.random=map[n2]

            #print(parent,child,n1,n2,lr)

            i+=3



        pInord(root)

        ansTree=cloneTree(root)
        pInord(ansTree)
        pInord(root)

        if ansTree==root:
            print(0)
        else:
            print(printInord(root,ansTree))




