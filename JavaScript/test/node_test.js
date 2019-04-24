const my_node = require('../my_node');
const chai = require('chai');

describe('MyNode', function() {
    describe('#init', function() {
        it('Correctly initializes instance of MyNode', () => {
            let n = new my_node.MyNode(3);
            chai.assert.instanceOf(n, my_node.MyNode, 'n is instance of MyNode');
        });

        it('Initializes with correct default values', () => {
            let n = new my_node.MyNode(3);
            chai.assert.strictEqual(n.key, 3);
            chai.assert.strictEqual(n.next_pointer, null);
        });
    });
});