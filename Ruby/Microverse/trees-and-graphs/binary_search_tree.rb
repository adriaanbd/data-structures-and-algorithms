# You will be given an array of numbers as input. 
# Insert the numbers (in order) one-at-a-time into a binary search tree. 
# Then return a string with the tree in pre-order

class Node
  attr_reader :data
  attr_accessor :left, :right

  def initialize(data)
    @data = data
  end
end

def array_to_tree(array, i = 0)
  return nil if i >= array.length || array[i].zero?

  node = Node.new(array[i])
  node.left = array_to_tree(array, 2 * i + 1)
  node.right = array_to_tree(array, 2 * i + 2)

  node
end

def pre_order(node)
  return '' if node.nil?

  "#{pre_order(node.left)} #{pre_order(node.right)} #{node.data} "
end

def binary_search_tree(array)
  tree = array_to_tree(array)
end

puts binary_search_tree([8, 3, 10, 1, 6, 14, 4, 7, 13])
# => "8 3 1 6 4 7 10 14 13"