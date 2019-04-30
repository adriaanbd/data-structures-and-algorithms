# How to Traverse a Tree

Trees are *not a linear data structure* like lists; so there is no clear way to traverse through them.

## Approaches to Tree Traversal

Mainly, we're trying to answer the following questions:

* Should we start at the left tree or the right tree? 
* Should we traverse one subtree or one section of the tree?
* Should we traverse everything at the same level first?

There are two (2) broad categories to tree traversal:

1. Depth First Search (DFS) - implies visiting *all child nodes of a subtree* before moving on to the next subtree.
2. Breadth First Search (BFS) - implies visiting *all nodes on the same level* before visiting child nodes. 

### Depth First Search (DFS)

There are also several approaches to DFS traversals.

Example Tree (fig 1):

​     		A
​		 /       \
​	      B 	    C
​	  / 	\
​       D   	  E
​			 \
​			   F

#### Pre-Order traversal

The general idea of the algorithm is to visit a node as soon as you see it before you traverse any further in the tree.  Visiting a node implies looking at the object's value.

**Algorithm**: 

1. Start at the root and visit it.
2. Pick one of its children (left by convention) and visit it.
3. Continue visiting all left most nodes until reaching a leaf.
4. Go back up to the leaf's parent, and visit its right child.
5. Continue until visiting all nodes of the left subtree.
6. Go back up to the root and visit its right child.
7. Continue visiting all left most nodes until reaching a leaf.
8. Go back up to the leaf's parent, and visit its right child.
9. Continue until visiting all nodes of the right subtree.

By following this algorithm, the tree in reference (fig 1) would've been visited in the following order: **A B D E F C**

#### In-Order traversal

The general idea of the algorithm is to visit the left most leaf node of a subtree before visiting any other node in tree. Note that visiting a node implies looking at the object's value.

**Algorithm:**

1. Start at the root.
2. Traverse the left most nodes of the left subtree until reaching a leaf.
3. Visit the leaf.
4. Visit its parent.
5. Traverse to the left most node of its right child until reaching a leaf.
6. No leaf found, traverse to parent and visit right child leaf.
7. Visit its parent.
8. Go back to the root and visit it.
9. Repeat the process on the right subtree.

By following this algorithm, the tree in reference (fig 1) would've been visited in the following order: **D B F E A C**

#### Post-Order traversal

The general idea of the algorithm is to visit all leaf nodes of a sub tree before visiting any other node in the subtree. Note that visiting a node implies looking at the object's value.

Algorithm:

1. Start at the root.
2. Traverse the left most nodes of the left subtree until reaching a leaf.
3. Visit the leaf.
4. Traverse to to its parent.
5. Traverse to the left most leaf node of its right child and visit it.
6. Traverse to its parent.
7. Visit its right child.
8. Traverse to the root.
9. Repeat the process on the right subtree.

By following this algorithm, the tree in reference (fig 1) would've been visited in the following order: **D F E B C A**

