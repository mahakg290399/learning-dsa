
import node
def sumOfLinkedListIterative(head):
    current = head
    sum = 0
    while current:
        sum += current.val
        current = current.next
    return sum

def sumOfLinkedListRecursive(head, sum):
    if not head : return 0
    return head.val + sumOfLinkedListRecursive(head.next, sum)

print(sumOfLinkedListRecursive(node.a, sum))
print(sumOfLinkedListIterative(node.a))