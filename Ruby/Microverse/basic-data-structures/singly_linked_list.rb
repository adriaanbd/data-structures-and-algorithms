load 'my_node.rb'

class LinkedList
  attr_accessor :head, :tail, :size

  def initialize
    @head = nil
    @tail = nil
    @size = 0
  end

  def add(node)
    node = MyNode.new(node)
    if @head.nil?
      @head = node
      @tail = node
    else
      @tail.next_pointer = node
    end
    @tail = node
    @size += 1
  end



  def add_at(index, node)
    node = MyNode.new(node)
    if index.zero? or @size.zero?
      node.next_pointer = @head
      @head = node
      @tail = node if @tail.nil?
    else
      raise IndexError if index > @size - 1

      current_node = @head.next_pointer
      @head.next_pointer = node if index == 1
      count = 1
      until count == index
        if count == index - 1
          next_node = current_node.next_pointer
          node.next_pointer = next_node
          current_node.next_pointer = node
        end
        current_node = current_node.next_pointer
        count += 1
      end
      node.next_pointer = current_node
    end
    @size += 1
  end

  def get(index)
    raise IndexError if index > @size - 1

    return @head.key if index.zero?

    return @tail.key if index == @size - 1

    current_node = @head.next_pointer
    return current_node.key if index == 1

    count = 0
    until count == index - 1
      current_node = current_node.next_pointer
      count += 1
    end
    current_node.key
  end

  def remove(index)
    raise IndexError if index > @size - 1

    if size == 1
      @head = nil
      @tail = nil
    else
      current_node = @head
      @head = current_node.next_pointer if index.zero?
      count = 0
      until count == index
        if count == index - 1
          next_node = current_node.next_pointer
          if index < @size - 1
            current_node.next_pointer = next_node.next_pointer
          else
            @tail = current_node
          end
        end
        current_node = current_node.next_pointer
        count += 1
      end
    end
    @size -= 1
  end

end

