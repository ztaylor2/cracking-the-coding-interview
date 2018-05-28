"""Test problem 4.1."""


def test_bfs_returns_true():
    """Test that the breadth first search method returns true."""
    from CTCI_4_1 import is_route
    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': [],
             'd': []}

    node1 = 'a'
    node2 = 'd'

    assert is_route(graph, node1, node2) is True
