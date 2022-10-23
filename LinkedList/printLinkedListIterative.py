import node
# iterative
def printLinkedList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

printLinkedList(node.a)