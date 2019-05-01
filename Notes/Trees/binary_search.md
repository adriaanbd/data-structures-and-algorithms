# Binary Search Trees (BST)

Trees are inherently unorganized. We know what the overall structure looks like, but we don't know where a specific element will be. However, if we add some rules to the ordering of elements in a tree, we could accomplish certain operations really fast. 

* When would you want to use these structures?

* What tasks would they speed up?

* What are the pros and cons of each approach?

## Concept

A BST is a type of Binary Tree because every parent node has at most two children, but the values are sorted in a particular order:

1. Every value on the right of a particular node is larger than it.
2. Every value on the left of a particular node is smaller than it.

The addition of these two rules speed up tree traversal operations such as search and delete.

## Example 

Consider following BST.

![File:Binary search tree.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)



### Search 

If we would like to find 7, the search operation algorithm would go something like this:

1. Start at the root and visit it.
2. Since seven (7) is smaller than the root, visit its left child.
3. Since seven (7) is greater than three (3), visit its right child.
4. Since seven (7) is greater than six (6), visit its right child.
5. Seven (7) is found!

The run time of a BST is equivalent to the height of the tree, which is O(log n), since the number of possible solutions decrease by half as we go down each level, in the same way the number of nodes in a level increase twice as much as the number of nodes in the previous level.

###  Insert

If we would like to insert the number 2, the insert operation is a search operation for either a leaf node or a node with only one child. The algorithm would go something like this:

1. Visit the root note.
2. Since two (2) is less than eight (8), visit its left child.
3. Since two (2) is greater than one (1), visit its right child.
4. Since right child is empty, insert two (2).

### Delete 

This operation is a little bit more complex, since it could involve some extra work implying re-arranging some nodes. For example, if we would like to delete 6 from the Tree, we would have to go through the search operation algorithm until we locate 6, delete it, and rearrange its children, placing either 4 or 7 as the right child of 3 and moving the remaining child either to the left of right.

## Balanced Vs. Unbalanced Trees

![How To Not Be Stumped By Trees – basecs – Medium](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn-images-1.medium.com%2Fmax%2F1600%2F1*zkYif_uQsOS80Zx7L0K9pg.jpeg&f=1)

An unbalanced Tree is skewed to one of the branches, meaning that either of its branches is longer than the other. The running time in this scenario is of a linear time O(n), whereas in a balanced Tree it is of O(log n).