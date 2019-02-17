class MyNode {
    constructor(key, next_pointer=null) {
        this.key = key;
        this.next_pointer = next_pointer;
    }
}

module.exports = { MyNode };

// let n = new MyNode(3);
// console.log(n.key, n.next_pointer);

// let s = new MyStack;
// console.log(s.head, s.min_stack, s.size);

// s.push(10);
// console.log(s.size, s.head.key, s.min_stack.key);

// s.push(20);
// console.log(s.size, s.head.key, s.min_stack.key);

// s.push(5);
// console.log(s.size, s.head.key, s.min_stack.key);

// console.log(5 === s.pop());
// console.log(s.size);
// console.log(s.min_stack.key);
// console.log(s.head.key);
