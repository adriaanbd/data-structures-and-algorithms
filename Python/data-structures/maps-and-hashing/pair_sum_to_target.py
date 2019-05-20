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


def better_pair_sum_to_zero(input_list: list, target: int):
    index_dict = dict()
    pair = list()
    for index, value in enumerate(input_list):
        remainder = target - value
        if index_dict.get(remainder) is not None:  # better
            pair.append(index_dict[remainder])
            pair.append(index)
        else:
            index_dict[value] = index  # better
    return pair


def test_function(test_case):
    output = better_pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, -4], -4, [0, 4]]
test_function(test_case_3)