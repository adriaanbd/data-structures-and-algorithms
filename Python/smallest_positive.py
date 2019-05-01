def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    if len(in_list) == 1:
        return None
    smallest = max(in_list)
    for num in in_list:
        if all([num < smallest, num > 0]):
            smallest = num
    return smallest

# Test cases

tests = [
    [4, -6, 7, 2, -4, 10],
    [.2, 5, 3, -.1, 7, 7, 6],
    [-46.41, -55.11, 40.64],
    [-3.53, -56.3, 11.17, -25.21, 96.21, -44.62, 94.95, 65.85, 26.79, -88.16], # 11.17
    [-98.35], # None
    [-33.04, 48.83, 75.33, 39.82, 76.38, 98.41, 71.27, 67.84, -16.58] # 39.82
]

for case in tests:
    print(smallest_positive(case))
    