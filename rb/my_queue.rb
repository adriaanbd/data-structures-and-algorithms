load 'my_node.rb'

class MyQueue
  attr_accessor :head, :tail, :size

  def initialize
    @tail = @head = nil
    @size = 0
  end

  def add(node)
    node = MyNode.new(node)
    @tail = @head = node if @head.nil?
    @tail.next_pointer = node
    @tail = node
    @size += 1
  end

  def remove
    return -1 if @size.zero?

    current_node = @head
    if @tail == @head
      @head = nil
      @tail = nil
      @size = 0
      current_node.key
    else
      @head = current_node.next_pointer
      @size -= 1
    end
    current_node.key
  end
end



