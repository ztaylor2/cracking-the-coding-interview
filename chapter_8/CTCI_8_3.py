"""Magic Index."""


def magic_index(a):  # O(n)
    """Determine the magic index of a."""
    for index, num in enumerate(a):
        if index == num:
            return index
