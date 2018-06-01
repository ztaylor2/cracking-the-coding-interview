"""Test 4.3."""

import sys
sys.path.insert(0, '/Users/zt/programming/interviews/interview-prep/cracking-the-coding-interview/data_structures')
from bst import BinarySearchTree, Node


# def test_list_of_depths():
#     """Test list of depths returns correctly."""
#     from CTCI_4_3 import list_of_depths
#     bst = BinarySearchTree()
#     bst.root = Node(5)
#     bst.root.left = Node(3)
#     bst.root.right = Node(7)
#     bst.root.left.left = Node(2)
#     bst.root.left.right = Node(4)
#     bst.root.right.left = Node(6)
#     bst.root.right.right = Node(8)
#     assert list_of_depths(bst) == [[5], [3, 7], [2, 4, 6, 8]]
