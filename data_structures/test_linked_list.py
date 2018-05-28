"""Test the linked list."""


def test_linked_list_push():
    """Test the push method of the linked list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    assert ll.head.val == 6
    assert ll.head.next.val == 5
    assert ll.head.next.next.val == 4
    assert ll.head.next.next.next.val == 3
    assert ll.head.next.next.next.next.val == 2
    assert ll.head.next.next.next.next.next.val == 1
    assert ll.head.next.next.next.next.next.next is None


def test_as_list_method():
    """Test the as list method of the linked list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    assert ll.as_list() == [6, 5, 4, 3, 2, 1]
