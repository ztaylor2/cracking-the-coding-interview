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


def one_away(string_1, string_2):
    """Determine if the two strings are one edit away."""
    # num_edits = abs(len(string_1) - len(string_2))
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

    if num_edits > 1:
        return False
    return True
