"""Test 1.3."""


def test_urlify():
    """Test the urlify method."""
    from CTCI_1_3 import urlify
    assert urlify('hi my name is zach') == 'hi%20my%20name%20is%20zach'
