"""Route Between Nodes: Given a directed graph, determine if there is a route between two nodes.

ex:

input:

    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': [],
             'd': []}

    node1 = 'a'
    node2 = 'd'

output:
    True

# perform a breadth first search or depth first search on node one, if
node two is found return True, else return False
"""


def is_route_bfs(graph, node1, node2):
    """Determine if there is a route between two nodes."""
    queue = [node1]
    visited_nodes = set()
    while queue:
        current_node = queue.pop(0)
        for child_node in graph[current_node]:
            if child_node not in visited_nodes:
                if child_node == node2:
                    return True
                queue.append(child_node)
        visited_nodes.add(current_node)
    return False


def is_route_dfs(graph, node1, node2):
    """Determine if there is a route between two nodes."""
    def dfs(current_node, visited_nodes):
        for child_node in graph[current_node]:
            if child_node not in visited_nodes:
                if child_node == node2:
                    return True
                return dfs(child_node, visited_nodes + [current_node])

    if dfs(node1, []):
        return True
    return False
