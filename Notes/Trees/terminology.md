# Things to know

1. Nodes in a tree have a parent-child relationship (they can only have one parent).
2. A Node in a lower level (i.e. closer to the root) is a parent, whereas node in a higher level is a child.
3. A node in the middle might be both a parent and a child and it is referred to as an internal node.
4. Nodes at the end (i.e. highest level) that have no children are called leaves.
5. Connections between nodes are called Edges, and a group of Edges is called a Path.
6. The height of a node is the number of Edges between the Node in reference and the furthest Leaf on the Tree (i.e. a leaf has a height of 0, but a parent of a leaf has a height of 1; and the height of the Tree overall is the height of the root node).
7. The Depth of a Node is the number of Edges to the Root.
8. Height and Depth move inversely (if a node is closer to a leaf then it's furthest to the root).

