def simple_quicksort(array)
  return array if array.empty? || array.one?
  
  pivot = array.shift
  left = []
  right = []

  array.each do |num|
    if num <= pivot
      left << num 
    else
      right << num 
    end
  end

  simple_quicksort(left) + [pivot] + simple_quicksort(right)
end

array = [5, 8, 1, 3, 7, 10, 2]
p simple_quicksort(array)