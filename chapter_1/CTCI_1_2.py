"""Given two strings write a method to determine if one is a
permutation of the other."""


def is_permutation(string_1, string_2):
    """Determine if string one is a permutation of string 2."""
    return sorted(string_1) == sorted(string_2)
