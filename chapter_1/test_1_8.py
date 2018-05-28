"""TEst 1.8."""


def test_zero_matrix():
    """Test zero matrix."""
    from CTCI_1_8 import zero_matrix
    input = [[1, 2, 3],
             [4, 5, 0],
             [4, 5, 6]]

    output = [[1, 2, 0],
              [0, 0, 0],
              [4, 5, 0]]
    assert zero_matrix(input) == output
