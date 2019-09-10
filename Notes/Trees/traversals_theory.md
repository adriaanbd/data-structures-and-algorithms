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

Since Trees are *not linear data structures* like lists, there is no clear way to traverse them.  In an effort to answer some of the following questions, there are two (2) broad categories to tree traversals that intend to answer the following questions:

* Should we start at the left subtree or the right subtree? 
* Should we traverse one subtree or a section of the tree before moving to the next one? 
* Or should we traverse everything at the same level first?

### Tree Traversal Categories

1. Depth First Search (DFS) - implies visiting *all child nodes of a subtree* before moving on to the next subtree or, in other words, if there are children to explore, visiting them first is a priority.
2. Breadth First Search (BFS) - implies visiting *all nodes on the same level* before visiting child nodes. 

#### Depth First Search (DFS)

There are several approaches to DFS traversals.

Example Tree:

 ![img](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.dEwNCti2QP7slYUr7E59KgHaGL%26pid%3DApi&f=1)

##### Preorder traversal

The general idea of the algorithm is to visit a node as soon as you see it, before you traverse any further in the tree.  Visiting a node implies looking at the object's value.

###### Algorithm: 

1. Visit root node.
2. If left AND right child *have been visited* OR *don't exist* AND *parent exists*, traverse to parent, else exit.
3. Visit left child if left child exists AND hasn't been visited until reaching a node with no left child
4. Visit right child if right child exists AND hasn't been visited.
5. Go to step 2.

By following this algorithm, the tree in reference (fig 1) is visited in the following order: **5 => 3 => 1 => 4 => 7 => 10**

##### Inorder traversal

The general idea of the algorithm is to visit the left most leaf node of a subtree before visiting any other node in tree. Note that visiting a node implies looking at the object's value. 

###### Algorithm

1. Start at root but don't visit it.
2. If left child exists and has not been visited:
	* Traverse to left child until reaching a leaf node.
	* Visit the leaf node.
	* Traverse and visit its parent node.
3. If right child exists and has not been visited:
	* Traverse to right child 
	* Visit the node if it is a leaf node
	* If it isn't a leaf node, go to step two (2).
4. Traverse to parent node until reaching root node.
5. Visit root node.
6. Go to step two (2).

By following this algorithm, the tree in reference (fig 1) is visited in the following order: 

**1 => 3 => 4 => 5 => 7 => 10**

##### Postorder traversal

The general idea of the algorithm is to *visit all leaf nodes of a sub tree* **before** visiting any other node in the subtree. Note that visiting a node implies looking at the object's value.

Algorithm:

1. Start at the root but don't visit it.
2. If left child exists and has not been visited:
	* Traverse to left child until reaching a leaf node.
	* Visit the leaf node.
	* Traverse to parent node but don't visit it.
3. If right child exists and has not been visited:
	* Traverse to right child 
	* Visit the node if it is a leaf node
	* If it isn't a leaf node, go to step two (2).
4. Traverse to parent
5. Visit the node if both child nodes have been visited
6. Go to step four (4) if not on root node.
7. If on root node, go to step three (3).

 By following this algorithm, the tree in reference (fig 1) would've been visited in the following order: ** 1 => 4 => 3 => 10 => 7 => 5 **
