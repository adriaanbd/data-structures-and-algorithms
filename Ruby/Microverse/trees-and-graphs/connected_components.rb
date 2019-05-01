# function to determine if all nodes in a graph are connected
def connected_graph?(graph)
  queue = [graph.keys[0]]
  visited = []
  until queue.empty?
    node = queue.shift
    visited << node unless visited.include?(node)
    queue += graph[node].reject { |item| visited.include?(item) }
  end
  return visited.sort == graph.keys
end
