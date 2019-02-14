load 'my_node.rb'

class MyStack
  attr_accessor :head, :size

  def initialize
    @head = nil
    @size = 0
  end

  def push(node)
    node = MyNode.new(node)
    @head = node if @head.nil?
    node.next_pointer = @head
    @head = node
    @size += 1
  end

  def top
    size.zero? ? nil : @head.key
  end

  def pop
    return nil if @size.zero?

    current_node = @head
    if @size == 1
      @size = 0
      @head = nil
    else
      current_node.key if @head.next_pointer.nil?
      @head = current_node.next_pointer
      @size -= 1
    end
    current_node.key
  end
end