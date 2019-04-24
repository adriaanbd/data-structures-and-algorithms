=begin 

How Tall is the Tree?
Can you find the height of a Binary Tree? The height is the number of Nodes from the Root to the lowest Leaf. The Tree does not need to be balanced.

Challenge
Return the height of the Tree.

Example

array_tree = [2, 7, 5, 2, 6, 0, 9]


puts binary_tree_height(array_tree)

=> 3
=end

def binary_tree_height(array_tree, i = 0)
  return 0 if array_tree[i].nil? || array_tree[i].zero?

  left_height = binary_tree_height(array_tree, 2 * i + 1)
  right_height = binary_tree_height(array_tree, 2 * i + 2)
  [left_height, right_height].max + 1
end

puts binary_tree_height([2, 7, 5, 2, 6, 0, 9])
# => 3