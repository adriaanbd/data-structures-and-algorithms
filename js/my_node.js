class MyNode {
    constructor(key, next_pointer=null) {
        this.key = key;
        this.next_pointer = next_pointer;
    }
}

class MyStack {
    constructor(head=null, min_stack=null, size=0) {
        this.head = head;
        this.min_stack = min_stack;
        this.size = size;
    };

    push(data) {
        const node = new MyNode(data);
        if (this.size === 0) {
            this.head = node;
            this.min_stack = new MyNode(data);
        } else if (node.key < this.min_stack.key) {
            let new_min = new MyNode(data);
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
        } else if (this.min_stack == this.head) {
            this.min_stack = this.min_stack.next_pointer;
        }
        this.head = current_node.next_pointer;
        this.size = this.size - 1;
        return current_node.key
    };

    top() {
        console.log(this.head);
    };

    min() {
        return this.min_stack.key
    };
}

let n = new MyNode(3);
console.log(n.key, n.next_pointer);

let s = new MyStack;
console.log(s.head, s.min_stack, s.size);

s.push(10);
console.log(s.size, s.head.key, s.min_stack.key);

s.push(20);
console.log(s.size, s.head.key, s.min_stack.key);

s.push(5);
console.log(s.size, s.head.key, s.min_stack.key);

console.log(5 === s.pop());
console.log(s.size);
console.log(s.min_stack.key);
console.log(s.head.key);
