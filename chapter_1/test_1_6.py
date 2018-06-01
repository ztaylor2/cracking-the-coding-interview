"""Test problem 1.6."""


def test_1_6():
    """Test string compression method."""
    from CTCI_1_6 import string_compression
    assert string_compression('aabcccccaaa') == 'a2b1c5a3'
