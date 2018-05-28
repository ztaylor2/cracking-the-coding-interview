"""List of Depths.

Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth.

(e.g., if you have a tree with depth D, you'll have D linked lists.)

# breadth first search, at each level create a linked list.
"""


import sys
sys.path.insert(0, '/Users/zt/programming/interviews/interview-prep/cracking-the-coding-interview/data_structures')
from linked_list import LinkedList


def list_of_depths(bst):
    """Create a linked list for every depth of the bst."""
    previous_level = []
    current_level = [bst.root]
    list_of_levels = [bst.root]

    while current_level:

        current_node = current_level.pop(0)

        if previous_level[-1] not in current_level:
            list_of_levels.append(current_level)
            previous_level = current_level

        if current_node.left:
            current_level.append(current_node.left)
        if current_node.right:
            current_level.append(current_node.right)

    return list_of_levels
