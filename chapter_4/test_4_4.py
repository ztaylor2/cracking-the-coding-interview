"""."""


class Node(object):
    """."""

    def __init__(self, val, left=None, right=None):
        """."""
        self.val = val
        self.left = left
        self.right = right


def test_4_4():
    """."""
    from CTCI_4_4 import check_bal_of_tree
    tree1 = Node(5, Node(3), Node(7))
    tree2 = Node(5, Node(3, Node(2, Node(1))))
    assert check_bal_of_tree(tree1) is True
    assert check_bal_of_tree(tree2) is False
