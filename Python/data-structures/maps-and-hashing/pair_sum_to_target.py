# Given an input_list and a target, return the indices of pair of integers 
# in the list that sum to the target. The best solution takes O(n) time. 
# You can assume that the list does not have any duplicates.


def pair_sum_to_zero(input_list, target):
    pair_sum = 0
    pair = []
    for index, value in enumerate(input_list):
        next_index = index + 1
        while index < len(input_list) - 1:
            pair_sum = value + input_list[next_index]
            if pair_sum == target:
                pair.append(index)
                pair.append(next_index)
            index += 1
    return pair