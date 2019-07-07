"""
Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
"""


def rearrange_digits(arr):
    sorted_arr = merge_sort(arr)
    
    l, r = '', ''
    for i, j in enumerate(sorted_arr):
        if i % 2 == 0:
            l += str(j)
        else:
            r += str(j)
    
    biggest_pairs = [l, r]
    return biggest_pairs


def merge_sort(arr):
    if len(arr) < 2:
        return
    
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    
    merge_sort(left)
    
    merge_sort(right)
    
    return merge_ascending(left, right, arr)


def merge_ascending(left, right, arr):
    
    left_idx = right_idx = main_idx = 0 
    
    while left_idx < len(left) and right_idx < len(right):
        
        left_val, right_val = left[left_idx], right[right_idx]
        
        if left_val >= right_val:
            arr[main_idx] = left_val
            left_idx += 1
        else:
            arr[main_idx] = right_val
            right_idx += 1
        
        main_idx += 1
    
    while left_idx < len(left):
        
        arr[main_idx] = left[left_idx]
        left_idx += 1
        main_idx += 1
    
    while right_idx < len(right):
        
        arr[main_idx] = right[right_idx]
        right_idx += 1
        main_idx += 1
    
    return arr


print(rearrange_digits([1, 2, 3, 4, 5]) == ['531', '42']) 
print(rearrange_digits([4, 6, 2, 5, 9, 8]) == ['964', '852']) 
