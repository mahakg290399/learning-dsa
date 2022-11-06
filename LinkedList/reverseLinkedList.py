import node

#iterative
def reverseLinkedListIterative(head):
    current = head
    prev = None
    while current:
        #Temprary string the value of current.next into next
        next = current.next
        #changing the direction of arrow
        current.next = prev
        #moving ahead
        prev = current
        current = next
    return prev.val

#recusive
def reverseLinkedListRecursive(head, prev = None):
    if not head: return prev.val
    next = head.next
    head.next = prev
    return reverseLinkedListRecursive(next, head)


print(reverseLinkedListRecursive(node.a))
print(reverseLinkedListIterative(node.a))