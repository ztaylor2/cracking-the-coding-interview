"""A linked list in python."""


class Node(object):
    """A node for a linked list."""

    def __init__(self, val, next=None):
        """Init the node."""
        self.val = val
        self.next = next


class LinkedList(object):
    """A linked list."""

    def __init__(self):
        """Init the linked list."""
        self.head = None

    def push(self, val):
        """Add a value to the front of the linked list."""
        self.head = Node(val, self.head)
