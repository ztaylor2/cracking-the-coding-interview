"""Test problem 1.1."""


def test_returns_false():
    """Test that the method returns false when it should."""
    from CTCI_1_1 import unique_charactors
    assert unique_charactors('aa') is False


def test_returns_true():
    """Test that the method returns true when it should."""
    from CTCI_1_1 import unique_charactors
    assert unique_charactors('ab') is True
