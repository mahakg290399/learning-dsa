import node


# recursive
def getNodeValueRecursive(head, idx):
    if head is None: return None
    if idx == 0: return head.val
    return getNodeValueRecursive(head.next, idx - 1)

# Iterative
def getNodeValueIterative(head, idx):
    current = head
    while current:
        if idx == 0: return current.val
        idx -= 1
        current = current.next
    return "Not found"


print(getNodeValueIterative(node.a, 7))
print(getNodeValueRecursive(node.a, 3))
