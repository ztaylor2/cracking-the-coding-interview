"""Test problem 4.1."""


def test_bfs_returns_true():
    """Test that the breadth first search method returns true."""
    from CTCI_4_1 import is_route_bfs
    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': [],
             'd': []}

    node1 = 'a'
    node2 = 'd'

    assert is_route_bfs(graph, node1, node2) is True


def test_bfs_returns_false():
    """Test that the breadth first search method returns false."""
    from CTCI_4_1 import is_route_bfs
    graph = {'a': ['b', 'c'],
             'b': ['c'],
             'c': ['a', 'b'],
             'd': ['a']}

    node1 = 'a'
    node2 = 'd'

    assert is_route_bfs(graph, node1, node2) is False


def test_dfs_returns_true():
    """Test that the depth first search method returns true."""
    from CTCI_4_1 import is_route_dfs
    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': [],
             'd': []}

    node1 = 'a'
    node2 = 'd'

    assert is_route_dfs(graph, node1, node2) is True
