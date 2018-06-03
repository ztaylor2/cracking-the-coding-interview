"""Delete middle node."""


def delete_middle_node(ll, node):
    """."""
    curr_node = ll.head
    while curr_node.next:
        if curr_node.next == node:
            break
        curr_node = curr_node.next
    curr_node.next = curr_node.next.next
