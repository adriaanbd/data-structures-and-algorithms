def count_words(phrase: str) -> dict:
    """
    Accepts a string and returns a mapping that has words as the keys and the number of times each word was seen as
    the values. It parses the string to lowercase and ignores punctuation.
    :param phrase: a phrase whose words will be counted
    :return: a dictionary with words as keys and number of times in phrase as values
    """
    count = dict()
    for item in phrase.lower().split():
        item = item.strip('?¿!.')
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
    return count
