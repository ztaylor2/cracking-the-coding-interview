"""Problem 1.1 in CTCI 6th Edition.

Implement an algorithm to determine if a string has all unique charactors. 
What if you can not use additional data structures?

ex:
'abcd'
"""


def unique_charactors(input_string):
    """Determine if a string has all unique charactors."""
    charactors_seen = set()
    for char in input_string:
        if char in charactors_seen:
            return False
        charactors_seen.add(char)
    return True
