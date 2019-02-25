load 'singly_linked_list.rb'

def transpose(string)
  l = LinkedList.new
  string.each_char do |char|
    l.add(char) if char != 'n'
    if l.tail.key == 'g'
      current = l.head
      index = 0
      unless current.next_pointer.key == 'g'
        current = current.next_pointer
        index += 1
      end
      l.add_at(index + 1, char)
    end
  end
  return l
end

string = 'rignadingdiggn!'
p transpose('gn')
p transpose(string)

# load 'my_node.rb'

# class NgLinkedList
#   attr_accessor :head, :tail, :size
#
#   def initialize
#     @head = nil
#     @tail = nil
#     @size = 0
#   end
#
#   def push(node)
#     node = MyNode.new(node)
#     if @tail.nil?
#       @tail = node
#       @head = @tail
#     elsif @head.key == 'g' && node.key == 'n'
#       if @size == 1
#         @tail = node
#         @tail.next_pointer = @head
#       else
#         current_node = @tail
#         ## Objective is to traverse list from tail until the letter before g, to insert the new node('n'):
#         # until current_node.next_pointer.key == 'g'
#         #   current_node = current_node.next_pointer
#         # end
#         next_node = current_node.next_pointer
#         current_node.next_pointer = node
#         node.next_pointer = next_node
#       end
#     else
#       @head.next_pointer = node
#       @head = node
#     end
#     @size += 1
#   end
# end