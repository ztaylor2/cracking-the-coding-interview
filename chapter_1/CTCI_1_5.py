"""One away.

There are three types of edits that can be performed on strings: insert
a charactor, remove a character, or replace a character. Given
two strings, write a function to check if they are one edit (or zero edits)
away.

ex:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

# brute force solution


def one_away(string_1, string_2):
    """Determine if the two strings are one edit away."""
    num_edits = 0
    string_1_contents = {}
    string_2_contents = {}
    for char in string_1:
        if char in string_1_contents:
            string_1_contents += 1
        else:
            string_1_contents[char] = 1
    for char in string_2:
        if char in string_2_contents:
            string_2_contents += 1
        else:
            string_2_contents[char] = 1
    for key in string_1_contents:
        if key not in string_2_contents:
            num_edits += string_1_contents[key]
    for key in string_2_contents:
        if key not in string_1_contents:
            num_edits += string_2_contents[key]

    if len(string_1) == len(string_2):
        num_edits -= 1

    if num_edits > 1:
        return False
    return True

# readable solution:


# def one_away(s1, s2):
#     '''Check if a string can converted to another string with a single edit'''
#     if len(s1) == len(s2):
#         return one_edit_replace(s1, s2)
#     elif len(s1) + 1 == len(s2):
#         return one_edit_insert(s1, s2)
#     elif len(s1) - 1 == len(s2):
#         return one_edit_insert(s2, s1)
#     return False


# def one_edit_replace(s1, s2):
#     edited = False
#     for c1, c2 in zip(s1, s2):
#         if c1 != c2:
#             if edited:
#                 return False
#             edited = True
#     return True


# def one_edit_insert(s1, s2):
#     edited = False
#     i, j = 0, 0
#     while i < len(s1) and j < len(s2):
#         if s1[i] != s2[j]:
#             if edited:
#                 return False
#             edited = True
#             j += 1
#         else:
#             i += 1
#             j += 1
#     return True
