"""Test 8.2."""


def test_8_2():
    """."""
    from CTCI_8_2 import robot_path
    grid = [[0, 1, 0],
            [0, 0, 0],
            [0, 1, 0]]
    assert robot_path(grid) == [['down', 'right', 'right', 'down']]
