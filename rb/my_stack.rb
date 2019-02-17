load 'my_node.rb'

class MyStack
  attr_accessor :head, :min_stack, :size

  def initialize
    @head = nil
    @min_stack = nil
    @size = 0
  end

  def push(node)
    node = MyNode.new(node)
    if @size.zero?
      @head = node
      @min_stack = node.dup
    elsif node.key < @min_stack.key # new node is less than min
      new_min = node.dup
      new_min.next_pointer = @min_stack # new min to last min node
      @min_stack = new_min # min node is now new node
    end
    node.next_pointer = @head if @size > 0
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
      @head = nil
      @min_stack = nil
    elsif @min_stack.key == @head.key
      @min_stack = @min_stack.next_pointer
    end
    @head = current_node.next_pointer
    @size -= 1
    current_node.key
  end

  def min
    return nil if @min_stack.nil?

    @min_stack.key
  end
end
