"""Remove Dups: Write code to remove duplicates from an unsorted linked list."""


def remove_dups(linked_list):
    """Remove duplicates from a linked list."""
    prev_node = None
    curr_node = linked_list.head
    vals_seen = set()
    while curr_node:
        if curr_node.val in vals_seen:
            prev_node.next = curr_node.next
            curr_node = curr_node.next
        else:
            vals_seen.add(curr_node.val)
            prev_node = curr_node
            curr_node = curr_node.next
