import node


def zipperLinkedListIterative(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0
    while current1 != None and current2 != None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else: 
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count+=1

    if current1: tail.next = current1
    if current2: tail.next = current2

    return head1

def zipperLinkedListRecursive(head1, head2):
    if not head2 and not head1: return None
    if not head1 : return head2
    if not head2 : return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipperLinkedListRecursive(next1, next2)
    return head1

def printll(head):
    while head:
        print(head.val)
        head=head.next


printll(zipperLinkedListIterative(node.a, node.n1))
printll(zipperLinkedListRecursive(node.a, node.n1))

