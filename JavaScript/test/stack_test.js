const my_stack = require('../my_stack');
const chai = require('chai');

describe('MyStack', function() {
    describe('#init', function() {
        it('Correctly initializes instance of MyStack', () => {
            const m = new my_stack.MyStack;
            chai.assert.instanceOf(m, my_stack.MyStack, 'n is instance of MyStack');
        });

        it('Initializes with correct default values', () => {
            const m = new my_stack.MyStack;
            chai.assert.strictEqual(m.size, 0, 'size is 0');
            chai.assert.strictEqual(m.head, null, 'head is null');
            chai.assert.strictEqual(m.min_stack, null, 'min_stack is null');
        })
    }),

    describe('#push', function() {
        it('Correctly pushes node to stack', () => {
            const m = new my_stack.MyStack;
            m.push(10)
            chai.assert.strictEqual(m.size, 1, 'size is 1');
            chai.assert.strictEqual(m.head.key, 10, 'head equals node.key');
            chai.assert.strictEqual(m.min_stack.key, 10, 'min_stack equals node.key')
        })

        it('Correctly pushes multiple nodes', () => {
            const m = new my_stack.MyStack;
            m.push(10);
            m.push(20);
            m.push(30);
            chai.assert.strictEqual(m.size, 3, 'size is 3');
            chai.assert.strictEqual(m.head.key, 30, 'head equals node.key');
            chai.assert.strictEqual(m.min_stack.key, 10, 'min_stack equals node.key');
        })

        it('Changes min after multiple pushes with intercalated min values', () => {
            const m = new my_stack.MyStack;
            m.push(10);
            m.push(20);
            m.push(30);
            chai.assert.strictEqual(m.min_stack.key, 10, 'min_stack equals new node.key');
            m.push(5);
            chai.assert.strictEqual(m.min_stack.key, 5, 'min_stack equals new node.key');
            m.push(7);
            m.push(9);
            m.push(4);
            chai.assert.strictEqual(m.min_stack.key, 4, 'min_stack equals new node.key');
            m.push(6);
            chai.assert.strictEqual(m.head.key, 6, 'head is equal to last node on stack')
        })
    }),

    describe('#pop', function() {
        it('Pops the only node and stack revert to defaults', () => {
            m = new my_stack.MyStack
            m.push(10)
            chai.assert.strictEqual(m.pop().key, 10, 'pop returns only node');
            chai.assert.strictEqual(m.size, 0);
            chai.assert.isNull(m.head, 'head is null');
            chai.assert.isNull(m.min_stack, 'min_stack is null');
        })
    })

    describe('#top', function() {
        it('Top returns head after multiple pushes', () => {
            m = new my_stack.MyStack
            m.push(10)
            chai.assert.strictEqual(m.top().key, 10, 'top returns only node');
            m.push(20)
            chai.assert.strictEqual(m.top().key, 20, 'top returns head');
            m.push(20)
            m.push(30)
            m.push(40)
            chai.assert.strictEqual(m.top().key, 40, 'top returns head after multiple pushes');
        })

        it('Top returns head after pop', () => {
            m = new my_stack.MyStack
            m.push(10)
            m.push(20)
            m.pop()
            chai.assert.strictEqual(m.top().key, 10, 'top returns only node');
        })
    })

    describe('#min', function() {
        it('Min returns node.key', () => {
            m = new my_stack.MyStack
            m.push(20)
            chai.assert.strictEqual(m.min(), 20, 'min returns only node.key');
            m.push(10)
            m.push(15)
            chai.assert.strictEqual(m.min(), 10, );
            m.push(5)
            m.push(12)
            m.pop()
            chai.assert.strictEqual(m.min(), 5, 'min returns node.key of head after pop of previous head');
        })

        it('Min returns node.key of node behind head', () => {
            m = new my_stack.MyStack
            m.push(20)
            m.push(10)
            m.push(15)
            m.push(5)
            m.push(12)
            m.pop()
            chai.assert.strictEqual(m.min(), 5, 'min returns node.key of head after pop of previous head');
        })

        it('Min returns node.key of head after pop of previous head', () => {
            m = new my_stack.MyStack
            m.push(20)
            m.push(10)
            m.push(15)
            m.push(5)
            m.push(12)
            m.pop()
            chai.assert.strictEqual(m.min(), 5, 'min returns node.key of head after pop of previous head');
        })
    })
});