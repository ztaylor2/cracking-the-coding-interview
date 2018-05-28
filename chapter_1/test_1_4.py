"""Test 1.4."""


def test_true():
    """Test that it returns true."""
    from CTCI_1_4 import palindrome_permutation
    assert palindrome_permutation('Tact Coa') is True


def test_false():
    """Test that it returns false."""
    from CTCI_1_4 import palindrome_permutation
    assert palindrome_permutation(';asldfjk') is False
