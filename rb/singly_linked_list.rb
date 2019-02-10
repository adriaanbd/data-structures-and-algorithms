load 'node.rb'

class LinkedList
  attr_accessor :head, :tail, :size

  def initialize
    @head = nil
    @tail = nil
    @size = 0
  end

  def add_to_back(node)
    if @head.nil?
      @head = node
      @tail = node
    else
      @tail.next_pointer = node
    end
    @tail = node
    @size += 1
  end

  def get_by_index(index)
    raise IndexError if index > @size - 1

    return @head.key if index.zero?

    return @tail.key if index == @size - 1

    current_node = @head.next_pointer
    return current_node.key if index == 1

    counter = 1
    until counter == index
      current_node = current_node.next_pointer
      counter += 1
    end
    current_node.key
  end
end
