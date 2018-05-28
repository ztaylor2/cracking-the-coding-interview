"""Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create abinary search tree with minimal height.

ex:

input = [2, 3, 4, 5, 6, 7, 8]

output =   5
        3      7
       2  4   6  8

# take middle of list and insert into tree, split list and insert middle again.
"""


def create_tree(input_list):
    """Create a tree given an input list."""
    tree_order = []
    next_lists = [input_list]
    while next_lists:
        current_list = next_lists.pop(0)
        middle_index = len(current_list) // 2
        if middle_index < len(current_list):
            tree_order.append(current_list[middle_index])
            next_lists.append(current_list[:middle_index])
            next_lists.append(current_list[middle_index + 1:])
    return tree_order



    # def rec_create_tree(input_list):
    #     """Create the smallest tree possible given the input list."""
    #     middle_index = len(input_list) // 2
    #     if middle_index < len(input_list):
    #         tree_order.append(input_list[middle_index])
    #         rec_create_tree(input_list[:middle_index])
    #         rec_create_tree(input_list[middle_index + 1:])

    # rec_create_tree(input_list)

    # return tree_order
