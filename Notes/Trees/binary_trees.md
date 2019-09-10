# Binary Trees

Binary Trees are trees were parents have at most two (2) children with no particular order; therefore, nodes can have anywhere from zero (0) to two (2) children.

To search for a node within a tree, one would need to traverse it using any of the previously mentioned traversal algorithms, mainly DFS (pre-order, in-order or post-order) or BFS (level-order).

## Search

Since searching through an unordered Tree would require visiting every single node until finding the desired element, a search operation has a worst-case running time of `O(n)`, typically called a linear time.

## Delete

A delete operation is a little bit more complex than a search operation and also has a linear time `O(n)`, as it would require: 

1. A search operation to locate the node to delete; and
2. Additional work to shift around the elements after deletion

## Insert

In contrast to a search or delete operation, an insert operation in an unordered Tree is easier, since we are just tucking a node onto a leaf or a parent with one child. Generally speaking, the algorithm for an insert operation implies:

1. Start at the root of a tree.
2. Traverse the tree until locating an open spot.

The worst case scenario for this algorithm is having to traverse a tree through the longest path (group of edges) until reaching the farthest leaf, which is the same thing as traversing the amount of nodes equal to the **height of the tree** or number of edges from root to farthest leaf. This implies a `O(n)` linear time complexity.


