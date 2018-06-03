"""."""


class Node(object):
    """."""

    def __init__(self, val, next=None):
        """."""
        self.val = val
        self.next = next


class LinkedList(object):
    """."""

    def __init__(self):
        """."""
        self.head = None


def test_2_3():
    """."""
    from CTCI_2_3 import delete_middle_node
    ll = LinkedList()
    node_to_delete = Node('c', Node('d'))
    ll.head = Node('a', Node('b', node_to_delete))
    delete_middle_node(ll, node_to_delete)
    assert ll.head.next.next.val == 'd'
