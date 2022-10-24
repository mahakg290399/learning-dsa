import node

#iterative
def findDataIterative(head, target):
    current = head
    while current:
        if current.val == target:
            return "Found"
        current = current.next
    return "Not Found"

# Recursive
def findDataRecursive(head, target):
    if not head: return "Not Found"
    if head.val == target: return "Found"
    return findDataRecursive(head.next, target)

print(findDataIterative(node.a, "E"))
print(findDataRecursive(node.a, "C"))