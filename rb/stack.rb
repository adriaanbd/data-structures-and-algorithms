load 'node.rb'

class Stack
  attr_accessor :head, :tail, :size

  def initialize
    @head = nil
    @size = 0
  end

  def push(node)
    node = Node.new(node)
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