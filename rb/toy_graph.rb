=begin
You will be given lists of numbers as input based on the above format. 
Then start from Node 0 and repeatedly visit the next connected node until you reach Node 4. 
You need to return an array with all the nodes visited.
=end

def graph(hash_graph, key = 0, visited = [])
	visited << key if visited.empty?
	val = hash_graph[key][0]
	visited << val
	graph(hash_graph, key = val, visited) unless val == 4
	return visited
end