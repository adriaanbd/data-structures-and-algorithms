const my_list = require('../my_linked_list');
const chai = require('chai');

describe('MyLinkedList', function() {
    describe('#init', function() {
        it('Correctly initializes instance of MyLinkedList', () => {
            const l = new my_list.MyLinkedList;
            chai.assert.instanceOf(l, my_list.MyLinkedList, 'Is an instance of MyLinkedList');
        }),

        it('Initializes with correct default values', () => {
            const l = new my_list.MyLinkedList;
            chai.assert.strictEqual(l.size, 0, 'size is 0');
            chai.assert.isNull(l.head, 'head is null');
            chai.assert.isNull(l.tail, 'tail is null')
        })
    }),

    describe('#add', function() {
        it('Add is a method of MyLinkedList', () => {
            const l = new my_list.MyLinkedList;
            chai.assert.isFunction(l.add);
        }),

        it('Add node to empy list', () => {
            const l = new my_list.MyLinkedList;
            l.add(10);
            chai.assert.strictEqual(l.size, 1, 'size is 1');
            chai.assert.strictEqual(l.head.key, 10, 'head is added node');
            chai.assert.strictEqual(l.tail.key, l.head.key, 'head and tail equal');
        }),

        it('Tail updates after multiple adds', () => {
            const l = new my_list.MyLinkedList;
            l.add(5);
            l.add(10);
            l.add(15);
            chai.assert.strictEqual(l.tail.key, 15, 'tail is last added node');
        }),

        it('Head remains after multiple adds', () => {
            const l = new my_list.MyLinkedList;
            l.add(5);
            l.add(10);
            l.add(15);
            chai.assert.strictEqual(l.head.key, 5, 'head is first added node');
        })
    }),

    describe('#get', function() {
        it('Get is a method of MyLinkedList', () => {
            const l = new my_list.MyLinkedList;
            chai.assert.isFunction(l.get);
        }),

        it('Returns tail and head by index', () => {
            const l = new my_list.MyLinkedList;
            l.add(10);
            chai.assert.strictEqual(l.head, l.get(0));
            l.add(15);
            chai.assert.strictEqual(l.tail, l.get(1));
        })
    })
})