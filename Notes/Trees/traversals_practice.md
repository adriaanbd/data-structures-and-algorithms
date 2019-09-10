# In Practice

To practice writing code for Trees and common Tree operations, one should be able to meet the following general objectives.

1. Binary Tree

   * Create a binary tree

2. Tree Traversals

   * DFS traversals
   * BFS traversals

3. Binary Search Tree operations

   * Insert a node
   * Search for a node
   * Delete a node

Furthermore, one should have a clear understanding of the average time complexity of all of the above.

## Creating a Binary Tree

To create a binary tree, meet the following requirements:

1. Node Class
	* Has a `value` attribute
	* Has a `left_child` attribute
	* Has a `right_child` attribute
	* Has `getter` and `setter` method for each attribute
	* Has a method to check for existance of `left_child` or `right_child`
2. Tree class
	* Has a `root` instance attribute of type `Node`
	* Its constructor can take in a node object or a can create a new Node with that value
	* Has a `getter` method that gets the roots