require 'minitest/autorun'
load 'node.rb'

class NodeTest < Minitest::Test
    def test_node_returns_node
        node = Node.new(1)
        assert_instance_of Node, node
    end

    def test_next_returns_nil
        node = Node.new(2)
        assert_nil node.next_pointer
    end

    def test_node_returns_key
        node = Node.new(3)
        assert_equal(3, node.key)
    end

    def test_next_pointer
        node1 = Node.new(4)
        node2 = Node.new(5)
        node1.next_pointer = node2
        assert_equal(node2, node1.next_pointer)
        assert_equal(5, node1.next_pointer.key)
    end

    def test_key_assignment
        node = Node.new(6)
        assert_raises(NoMethodError) { node.key = 7 }
    end
end