class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

nodeA = Node(3)
nodeB = Node(11)
nodeC = Node(4)
nodeD = Node(4)
nodeE = Node(2)
nodeF = Node(1)

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.right = nodeF