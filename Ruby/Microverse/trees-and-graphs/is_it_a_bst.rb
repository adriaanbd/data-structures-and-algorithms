=begin
Credit goes to GeekFoGeek's explanation: 
https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/ 

and Tushar Roy's YouTube video here:
https://www.youtube.com/watch?v=MILxfAbIhrE
=end 

MINI = -1000
MAXI = 1000

class Node
  attr_reader :data
  attr_accessor :left, :right

  def initialize(data)
    @data = data
  end
end

def array_to_tree(array, idx)
  return nil if idx >= array.length || array[idx].zero?

  node = Node.new(array[idx])

  node.left = array_to_tree(array, 2 * idx + 1)
  node.right = array_to_tree(array, 2 * idx + 2)

  node
end

def search_tree?(tree)
  tree = array_to_tree(tree, 0)
  search_tree_util(tree, MINI, MAXI)
end

def search_tree_util(node, mini, maxi)
  return true if node.nil?

  return false if node.data < mini || node.data > maxi

  search_tree_util(node.left, mini, node.data - 1) && search_tree_util(node.right, node.data + 1, maxi)
end

puts search_tree?([10, 4, 12])
# => true

puts search_tree?([10, 5, 7])
# => false