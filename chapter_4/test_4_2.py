"""Test CTCI 4.2."""


def test_create_tree_returns_correct_order():
    """Test that the create tree method returns the correct order."""
    from CTCI_4_2 import create_tree
    assert create_tree([2, 3, 4, 5, 6, 7, 8]) == [5, 3, 7, 2, 4, 6, 8]
