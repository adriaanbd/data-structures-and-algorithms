# Pre-order Traversal

## Using a Stack

Remember that a Stack is a Last In First Out (LIFO) abstract data type, which makes it a good fit for a pre-order traversal.

The algorithm would go something like this:

1. Push root node to stack.
2. Check if it has a left child.
3. If so, push left child and visit it.
4. Repeat from Step 2 unless no left child.
5. Check if it has a right child
6. If so, push right child and visit it.
7. Repeat from Step 2, unless no left or right child
8. Pop item from Stack (since we're done and it is a leaf node)
9. Assign node variable to the item at the Top of the Stack.
10. Repeat from Step 5, unless no left or right child.
11. Pop item from Stack (since we're done).
12. Stack should be empty

