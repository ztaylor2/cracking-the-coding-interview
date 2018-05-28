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

    def as_list(self):
        """Return the linked list as a list for easy testing."""
        curr_node = self.head
        ll_list = []
        while curr_node:
            ll_list.append(curr_node.val)
            curr_node = curr_node.next
        return ll_list
