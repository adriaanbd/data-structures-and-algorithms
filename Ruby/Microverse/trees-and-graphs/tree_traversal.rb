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

def post_order(node)
  return '' if node.nil?

  "#{post_order(node.left)} #{post_order(node.right)} #{node.data}"
end

tree = array_to_tree([10, 1, 2, 3, 4, 5, 6])
puts post_order(tree)