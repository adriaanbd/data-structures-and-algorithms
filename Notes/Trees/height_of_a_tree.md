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

The relationship of number of nodes in a Tree to number of levels `L` in a tree is that of a log 2, since 5 levels imply `2**L - 1`. The subtraction of `1` is executed because the root level has one (1) node. But the Height of a Tree consisting of levels `L` is always `L - 1`, because `height` is the *number of edges* from `root` to `leaf`, and in the case of a 5 leveled tree consisting of 31 nodes, the amount of edges from the Root to a Leaf is 4.