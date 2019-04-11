# My Solution
def depth_first_search(graph)
  search_queue = Array.new(1, graph.keys.first)
  visited = Array.new
  until search_queue.empty?
    node = search_queue.shift
    visited << node unless visited.include?(node)
    children = graph[node].select { |child| !visited.include?(child) }
    search_queue = search_queue.unshift(children).flatten
  end
  visited
end

# Model Solution (seen after)

# def depth_first_search(graph)
#   result = []
#   stack = [0]
#   visited = []
  
#   while stack.size != 0
#     head = stack.pop
#     result << head
#     visited << head
    
#     not_visited = graph[head].reject { |node| visited.include? node }
    
#     visited += not_visited
#     stack += not_visited.reverse
#   end
  
#   result
# end
