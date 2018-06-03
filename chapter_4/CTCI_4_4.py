"""Check if a binary tree is balanced."""


def check_bal_of_tree(node):
    """."""
    if node is None:
        return True

    to_visit = [node]

    while to_visit:
        curr_node = to_visit.pop(0)
        if check_bal_of_node(curr_node) > 1:
            return False
        if curr_node.left:
            to_visit.append(curr_node.left)
        if curr_node.right:
            to_visit.append(curr_node.right)

    return True


def check_bal_of_node(node):
    """."""
    right_height = height(node.right)
    left_height = height(node.left)
    return abs(right_height - left_height)


def height(node):
    """."""
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1
