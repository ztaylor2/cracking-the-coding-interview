"""Palindrome Permutation: given a string, write a funciton to check if it is a permutation of a palindrome. A palindrome is a word of phrase that is the same forward and backwards. a permutation is a rearrangement of letters. the palindrome does not need to be limited to just dictionary words.

ex:

input: Tact Coa

output: True (permutations: "taco cat", "atco cta", etc.)


Hypythysis: if input is even you need even numer of every letter.
if input is odd you need even number of ever letter except one. 


"""


def palindrome_permutation(input_string):
    """Check if it is a permutation of a palindrome."""
    input_string = input_string.lower().replace(' ', '')
    letters = {}
    for letter in input_string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    if len(input_string) % 2 == 0:
        expected_number_odd = 0
    else:
        expected_number_odd = 1

    number_odd = 0
    for letter in letters:
        if letters[letter] % 2 != 0:
            number_odd += 1

    return number_odd == expected_number_odd
