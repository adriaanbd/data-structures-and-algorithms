def insertion_sort(array)
  insertions = 0
  len = array.length - 1
  indices = [*1..len]
  indices.each do |idx|
    key = array[idx]
    j = idx - 1
    while j >= 0 && array[j] > key
      array[j + 1] = array[j]
      j -= 1
    end
    array[j + 1] = key
    p "Insert => #{array}"
    insertions += 1
  end
  array
end

p insertion_sort([2, 1, 3, 1, 2])
p insertion_sort([1, 4, 3, 6, 9, 2])
