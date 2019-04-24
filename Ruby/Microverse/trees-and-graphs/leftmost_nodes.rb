# The input for this challenge will provide an array of numbers in the above "breadth-first" format, and use 0's for non-nodes.
# Can you print out the sum of the Leftmost side of the Tree?
def leftmost_nodes_sum(array, i = 0, r = 0)
  idx = (2 * i) + 1
  left_node_idx = idx > array.length - 1 ? nil : idx
  return r + array[0] if left_node_idx.nil?
  
  r += array[idx]
  leftmost_nodes_sum(array, left_node_idx, r) 
end

puts leftmost_nodes_sum([2, 7, 5, 2, 6, 0, 9]) # 11
puts leftmost_nodes_sum([1, 7, 5, 2, 6, 0, 9, 3, 7, 5, 11, 0, 0, 4, 0]) # 13
puts leftmost_nodes_sum([5, 3, 4, 11, 13, 15, 21, 10, 4, 7, 2, 8, 0, 9, 0]) # 29
