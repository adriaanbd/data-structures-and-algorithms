def find_pairs(array, target)
  idxs = {}
  pairs = []
  array.each_with_index do |n, i| 
    remainder = target - n
    idx = idxs[remainder]
    idx.nil? ? idxs[n] = i : pairs << [array[idx], n] 
  end
  pairs
end

p find_pairs([1, 9, 11, 13, 2, 3, 7], 12)
# => [[1, 11], [9, 3]]