from copyreg import constructor
import node
# Recursive
def printLinkedList(head):
    if head == None: return
    print(head.val)
    printLinkedList(head.next)

printLinkedList(node.a)