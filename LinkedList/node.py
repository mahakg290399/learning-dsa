class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
class charNode(Node):
    def __init__(self, val: object) -> None:
        super().__init__(val)
        
a = charNode('A')
b = charNode('B')
c = charNode('C')
d = charNode('D')

a.next=b
b.next=c
c.next=d

class numNode(Node):
    def __init__(self, val) -> None:
        super().__init__(val)

n1 =  numNode(4)
n2 = numNode(6)
n3 = numNode(3)
n4 = numNode(7)

n1.next=n2
n2.next=n3
n3.next=n4

