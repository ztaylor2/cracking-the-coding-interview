"""A binary search tree."""


class Node(object):
    """A bst node."""

    def __init__(self, val, left=None, right=None):
        """Init the BST node."""
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """A bst."""

    def __init__(self):
        """Init the BST."""
        self.root = None
