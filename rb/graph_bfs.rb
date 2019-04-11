=begin
BFS goes through the Nodes one level at a time, 
so you need a structure to keep track of the next nodes to be processed.
Return an array with the given graph in BFS order.
=end

def bfs(graph)
  root = graph.keys[0]
  search_queue = [root]
  search_queue += graph[root]
  answer = []
  until answer.sort == graph.keys
    node = search_queue.shift
    answer << node unless answer.include?(node)
    search_queue += graph[node]
  end
  answer
end

g = {
  0 => [2],
  1 => [4],
  2 => [5, 0, 3],
  3 => [2],
  4 => [1, 5],
  5 => [4, 2]
}

p bfs(g) == [0, 2, 5, 3, 4, 1]
# => [0, 2, 5, 3, 4, 1]