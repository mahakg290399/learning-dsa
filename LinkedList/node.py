class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next=b
b.next=c
c.next=d

