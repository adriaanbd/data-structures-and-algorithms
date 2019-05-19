def bad_hash(string: str) -> int:
    """Returns the ASCII value sum of all chars in string.
       Prone to hash collisions."""
    hash_code = 0
    for char in string:
        hash_code += ord(char)
    return hash_code


def better_hash(string: str) -> int:
    """Generates a hash out of a character in a string by multipliying
       its ASCII value by a coefficient that increases exponentially
       after each character. Collisions are less likely."""
    hash_code = 0
    value = 37
    coefficient = 1
    for char in string:
        hash_code += ord(char) * coefficient
        coefficient *= value
    return hash_code


def hash_with_compression(string: str) -> int:
    hash_code = 0
    value = 37
    coefficient = 1
    for char in string:
        hash_code += ord(char) * coefficient
        hash_code %= 10
        coefficient *= value
        coefficient %= 10
    return hash_code % 10
