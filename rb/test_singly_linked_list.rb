require 'minitest/autorun'
load 'singly_linked_list.rb'
load 'node.rb'

class SinglyLinkedListTest < MiniTest::Test
  def test_init_returns_linked_list
    l = LinkedList.new
    assert_instance_of(LinkedList, l)
  end

  def test_init_vars_defaults
    l = LinkedList.new
    assert_nil(l.head)
    assert_nil(l.tail)
    assert_equal(0, l.size)
  end

  def test_add_to_back_first_node
    l = LinkedList.new
    node = Node.new(1)
    l.add_to_back(node)
    assert_equal(node, l.head)
    assert_equal(l.head, l.tail)
    assert_equal(1, l.size)
  end

  def test_next_pointer
    l = LinkedList.new
    node1 = Node.new(1)
    node2 = Node.new(2)
    l.add_to_back(node1)
    l.add_to_back(node2)
    assert_equal(node2, node1.next_pointer)
    assert_equal(node2.key, node1.next_pointer.key)
  end

  def test_is_head_and_tail
    l = LinkedList.new
    node1 = Node.new(1)
    node2 = Node.new(2)
    l.add_to_back(node1)
    l.add_to_back(node2)
    assert_equal(node1, l.head)
    assert_equal(node2, l.tail)
    assert_equal(node1.key, l.head.key)
    assert_equal(node2.key, l.tail.key)
  end

  def test_head_vs_tail
    l = LinkedList.new
    node1 = Node.new(1)
    node2 = Node.new(2)
    l.add_to_back(node1)
    l.add_to_back(node2)
    assert(l.head != l.tail)
  end

  def test_get_head_by_index
    l = LinkedList.new
    node = Node.new(1)
    l.add_to_back(node)
    assert_equal(node.key, l.get_by_index(0))
  end

  def test_index_vs_size
    l = LinkedList.new
    node1 = Node.new(1)
    l.add_to_back(node1)
    index = 0
    assert(l.size - index == 1)
  end

  def test_get_tail_by_index
    l = LinkedList.new
    node1 = Node.new(1)
    node2 = Node.new(2)
    l.add_to_back(node1)
    l.add_to_back(node2)
    assert_equal(node2.key, l.get_by_index(1))
  end

  def test_get_raise_index_error
    l = LinkedList.new
    node1 = Node.new(1)
    l.add_to_back(node1)
    assert_raises(IndexError) { l.get_by_index(1) }
  end

  def test_get_by_index
    l = LinkedList.new
    node1 = Node.new(1)
    node2 = Node.new(2)
    node3 = Node.new(3)
    node4 = Node.new(4)
    l.add_to_back(node1)
    l.add_to_back(node2)
    l.add_to_back(node3)
    l.add_to_back(node4)
    assert_equal(node3.key, l.get_by_index(2))
    assert_equal(node2.key, l.get_by_index(1))
    assert_equal(node1.key, l.get_by_index(0))
    assert_equal(node4.key, l.get_by_index(3))
  end

end