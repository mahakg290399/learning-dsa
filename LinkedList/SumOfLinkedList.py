
import node
def sumOfLinkedListIterative(head):
    current = head
    sum = 0
    while current:
        sum += current.val
        current = current.next
    return sum

def sumOfLinkedListRecursive(head):
    if not head : return 0
    return head.val + sumOfLinkedListRecursive(head.next)

print(sumOfLinkedListRecursive(node.n1))
print(sumOfLinkedListIterative(node.n1))