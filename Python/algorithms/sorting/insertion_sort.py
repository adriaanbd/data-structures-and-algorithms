def insertion_sort(array):
    for idx in range(1, len(array) - 1):
        key = array[idx]
        moving_idx = idx - 1
        while moving_idx >= 0 and array[moving_idx] > key:
            array[moving_idx + 1] = array[moving_idx]
            moving_idx -= 1
        array[moving_idx + 1] = key
        print(f'Insert No. {idx} => {array}')
    return array


print(insertion_sort([1, 4, 3, 6, 9, 2]))
# => 1 4 3 6 9 2
#    1 3 4 6 9 2
#    1 3 4 6 9 2
#    1 3 4 6 9 2
#    1 2 3 4 6 9