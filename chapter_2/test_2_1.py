"""Test 2.1."""

import sys
sys.path.insert(0, '/Users/zt/programming/interviews/interview-prep/cracking-the-coding-interview/data_structures')
from linked_list import LinkedList


def test_removes_val():
    """Test that the remove dup function removes duplicates."""
    from CTCI_2_1 import remove_dups
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    remove_dups(ll)
    assert ll.as_list() == [6, 5, 4, 3, 2, 1]
