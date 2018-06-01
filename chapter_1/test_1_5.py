"""Test problem 1.5."""


def test_1_5():
    """Test problem 1.5."""
    from CTCI_1_5 import one_away
    assert one_away('pale', 'ple') is True
    assert one_away('pales', 'pale') is True
    assert one_away('pale', 'bale') is True
    assert one_away('pale', 'bake') is False
