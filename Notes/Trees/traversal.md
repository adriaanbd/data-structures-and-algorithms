# Tree Traversal

## Notion

Generall speaking, the word Traverse means to:

* travel or pass across, over or through.
* move to and from, over, across and recross.
* go up, down or across.

*Traversal* is the act, product or result of *traversing*. Thus it is implied that a **Tree Traversal** is the act of moving through a Tree.

## Concept

A Tree Traversal implies *visiting* or *seeing* all the nodes of a tree at least once. To *see* or to *visit* is to *know* or be *able to know* the internal structure or data of a node. Therefore, if a node has a value of 3, a left child of 4 and a right child of 5, by *visiting* this node, we'd be able to *see* this data by calling `node.value`, `node.left` or `node.right`.

Tree Traversals are used for *searching*, *inserting*, or *deleting* nodes.

## How to Traverse a Tree

Since Trees are *not linear data structures* like lists, there is no clear way to traverse them.  In an effort to answer some of the following questions, there are two (2) broad categories to tree traversals. 

* Should we start at the left subtree or the right subtree? 
* Should we traverse one subtree or a section of the tree before moving to the next one? 
* Or should we traverse everything at the same level first?

## Tree Traversal Categories

1. Depth First Search (DFS) - implies visiting *all child nodes of a subtree* before moving on to the next subtree.
2. Breadth First Search (BFS) - implies visiting *all nodes on the same level* before visiting child nodes. 

### Depth First Search (DFS)

There are also several approaches to DFS traversals.

Example Tree:

 ![img](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.dEwNCti2QP7slYUr7E59KgHaGL%26pid%3DApi&f=1)

#### Preorder traversal

The general idea of the algorithm is to visit a node as soon as you see it before you traverse any further in the tree.  Visiting a node implies looking at the object's value.

**Algorithm**: 

1. Start at the root and visit it.
2. Check if there is a left child.
3. If left child exists, visit it, repeat from step 2.
4. Check if there is a right child.
5. If right child exists, visit it
6. Repeat from step 2.
6. Traverse to parent.
7. Repeat from step 4.

By following this algorithm, the tree in reference (fig 1) would've been visited in the following order: **5 3 1 4 7 10**

#### Inorder traversal

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

#### Postorder traversal

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
