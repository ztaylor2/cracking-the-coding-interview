"""Test problem 1.2."""


def test_permutations_true():
    """Test that the permutaiton method returns true correctly."""
    from CTCI_1_2 import is_permutation
    assert is_permutation('abcdefg', 'gfedcba') is True


def test_permutation_false():
    """Test that a permutation returns false correctly."""
    from CTCI_1_2 import is_permutation
    assert is_permutation('string_1', 'string_2') is False
