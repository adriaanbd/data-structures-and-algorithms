def tail(sequence_or_iterable, n: int) -> list:
    """
    Takes a sequence or an iterable and returns its last n elements if n isn't negative else returns empty list.
    :param sequence_or_iterable: Source of the n last elements operation.
    :param n: Count representation of the amount of elements to be retrieved from the tail.
    :return: A list representing the result of the last n elements operation from the first param.
    """
    if n < 1:
        return list()
    nums = [*sequence_or_iterable]
    if len(nums) == n:
        return list(nums)
    return nums[-n:]
