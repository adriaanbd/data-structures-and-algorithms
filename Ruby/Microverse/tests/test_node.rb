require 'minitest/autorun'
load 'my_node.rb'

class NodeTest < Minitest::Test
    def test_node_returns_node
        node = MyNode.new(1)
        assert_instance_of MyNode, node
    end

    def test_next_returns_nil
        node = MyNode.new(2)
        assert_nil node.next_pointer
    end

    def test_node_returns_key
        node = MyNode.new(3)
        assert_equal(3, node.key)
    end

    def test_next_pointer
        node1 = MyNode.new(4)
        node2 = MyNode.new(5)
        node1.next_pointer = node2
        assert_equal(node2, node1.next_pointer)
        assert_equal(5, node1.next_pointer.key)
    end

    def test_key_assignment
        node = MyNode.new(6)
        assert_raises(NoMethodError) { node.key = 7 }
    end
end