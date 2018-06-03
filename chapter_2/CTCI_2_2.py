"""."""


def kth_to_last(k, node):
    """."""
    curr_node = node
    kth_to_last_nodes = []
    for _ in range(k):
        if not curr_node.next:
            raise ValueError('k larger than list')
        curr_node = curr_node.next

    while curr_node:
        kth_to_last_nodes.append(curr_node.val)
        curr_node = curr_node.next

    return kth_to_last_nodes
