const my_node = require('./my_node');

class MyStack {
    constructor(head=null, min_stack=null, size=0) {
        this.head = head;
        this.min_stack = min_stack;
        this.size = size;
    };

    push(data) {
        const node = new my_node.MyNode(data);
        if (this.size === 0) {
            this.head = node;
            this.min_stack = {...node};
        } else if (node.key < this.min_stack.key) {
            let new_min = {...node};
            new_min.next_pointer = this.min_stack;
            this.min_stack = new_min;
        } else if (this.size > 0) {
            node.next_pointer = this.head;
        }
        this.head = node;
        this.size++;
    };

    pop() {
        if (this.size === 0) {return null};
        let current_node = this.head;
        if (this.size === 1) {
            this.head = null;
            this.min_stack = null;
            this.size = this.size - 1;
            return current_node;
        } else if (this.min_stack.key == this.head.key) {
            this.min_stack = this.min_stack.next_pointer;
        }
        this.head = current_node.next_pointer;
        this.size = this.size - 1;
        return current_node.key
    };

    top() {
        return this.head
    };

    min() {
        return this.min_stack.key
    };
}

module.exports = { MyStack }