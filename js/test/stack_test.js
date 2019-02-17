const my_stack = require('../my_stack');
const chai = require('chai');

describe('MyStack', function() {
    describe('#init', function() {
        it('Correctly initializes instance of MyStack', () => {
            let m = new my_stack.MyStack;
            chai.assert.instanceOf(m, my_stack.MyStack, 'n is instance of MyStack');
        });

        it('Initializes with correct default values', () => {
            let m = new my_stack.MyStack;
            chai.assert.strictEqual(m.size, 0, 'size is 0');
            chai.assert.strictEqual(m.head, null, 'head is null');
            chai.assert.strictEqual(m.min_stack, null, 'min_stack is null');
        });
    });
});