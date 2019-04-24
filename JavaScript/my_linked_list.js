const my_node = require('./my_node');

class MyLinkedList {
    constructor(head=null, tail=null, size=0) {
        this.head = head;
        this.tail = tail;
        this.size = size;
    };

    add(data) {
        const node = new my_node.MyNode(data);
        if (this.size === 0) {
            this.head = node;
        } else {
            this.tail.next_pointer = node;
        }
        this.tail = node;
        this.size++;
    }

    get(index) {
        if (index === this.size - 1) { return this.tail }
        else if (index === 0) { return this.head };
    }
}

module.exports = { MyLinkedList }