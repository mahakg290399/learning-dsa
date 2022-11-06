import node


def zipperLinkedList(head1, head2):
    current1 = head1
    current2 = head2
    tail = node.Node(None)
    while True:
        if (current1 is not None) OR (current2 is not None): break
        if current1:
            tail.val = current1.val
            if current2:
                tail.next = current2
            else:
                tail.next = current1.next
        if current2:
            tail.val = current2.val
            if current1:
                tail.next = current1
            else:
                tail.next = current2.next
        print(tail.val, tail.next)


zipperLinkedList(node.a, node.n1)
