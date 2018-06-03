"""."""


class Node(object):
    """."""

    def __init__(self, val, next=None):
        """."""
        self.val = val
        self.next = next


def test_2_2():
    """."""
    from CTCI_2_2 import kth_to_last
    head = Node('a', Node('b', Node('c', Node('d'))))
    assert kth_to_last(2, head) == ['c', 'd']
