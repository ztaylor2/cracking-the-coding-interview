"""String Compression.

Implement a method to perform basic string compression using the counts
of repeated characters.

Example:

input: 'aabcccccaaa'

output: 'a2b1c5a3'

If the compressed string is not smaller than the original string,
return the original string.
"""


def string_compression(input_string):
    """Perform a string compression on the input string."""
    compressed_string = ''
    char_count = 1
    prev_char = ''
    for char in input_string:
        if char == prev_char:
            char_count += 1
        else:
            compressed_string = compressed_string + str(char_count) + char
            char_count = 1
        prev_char = char

    return compressed_string[1:] + str(char_count)
