# Binary Trees

Binary Trees are trees were parents have at most two (2) children with no particular order; therefore, nodes can have anywhere from zero (0) to two (2) children.

To search for a node within a tree, one would need to traverse it using any of the previously mentioned traversal algorithms, mainly DFS (pre-order, in-order or post-order) or BFS (level-order).

## Search

Since searching through an unordered Tree would require visiting every single node until finding the desired element, a search operation has a worst-case running time of O(n), typically called a linear time.

## Delete

A delete operation is a little bit more complex than a search operation and also has a linear time O(n), as it would require: 

1. A search operation to locate the node to delete; and
2. Additional work to shift around the elements after deletion

## Insert

In contrast to a search or delete operation, an insert operation in an unordered Tree is easier, since we are just tucking a node onto a leaf or a parent with one child. Generally speaking, the algorithm for an insert operation implies:

1. Start at the root of a tree.
2. Traverse the tree until locating an open spot.

The worst case scenario for this algorithm is having to traverse a tree through the longest path (group of edges) until reaching the farthest leaf, which is the same thing as traversing the amount of nodes equal to the **height of the tree** or number of edges from root to farthest leaf.

## Height of a Tree

To understand the concept of the height of a tree we need to conceptualize two (2) *perfect* trees of three (3) and seven (7) nodes, respectively. *A perfect tree* is a tree that has all of its children (left and right), like this one:

![Binary tree](https://i.stack.imgur.com/ZsiDW.png)



* A Tree of three (3) nodes has a Root, a left child and a right child. It consists of two (2) levels.

* A Tree of seven (7) nodes has a Root, a perfect left subtree and a perfect right subtree. It consists of three (3) levels.

If you think about the maximum amount of nodes that a parent can hold per tree level, we can conclude that each level has the capacity to hold a number of nodes equivalent to a power of two (2). The reasoning behind this is simple: each node can have two children, so each new level can have twice as many nodes as the one before it, which implies that the number of nodes `n` per Level increase at a rate of `n * 2`.

Take a look at the following table.

| Level | Nodes in Level | Total Nodes in Tree |
| ----- | -------------- | ------------------- |
| 1     | 1              | 1                   |
| 2     | 2              | 3                   |
| 3     | 4              | 7                   |
| 4     | 8              | 15                  |
| 5     | 16             | 31                  |

The relationship of number of nodes in a Tree to number of levels `L` in a tree is that of a log 2, since 5 levels imply 2**L - 1. The subtraction of 1 is executed because the root level has one (1) node. But the height of a Tree consisting of levels `L` is always `L` - 1, because height is the number of edges from Root to Leaf, and in the case of a 5 leveled tree consisting of 31 nodes, the amount of edges from the Root to a Leaf is 4.



