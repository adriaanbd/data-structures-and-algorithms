require 'minitest/autorun'
load 'singly_linked_list.rb'

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

  def test_add_first_node
    l = LinkedList.new
    l.add(1)
    assert_equal(1, l.head.key)
    assert_equal(l.head, l.tail)
    assert_equal(1, l.size)
  end

  def test_next_pointer
    l = LinkedList.new
    l.add(1)
    l.add(2)
    assert_equal(2, l.head.next_pointer.key)
  end

  def test_is_head_and_tail
    l = LinkedList.new
    l.add(1)
    l.add(2)
    assert_equal(1, l.head.key)
    assert_equal(2, l.tail.key)
  end

  def test_head_vs_tail
    l = LinkedList.new
    l.add(1)
    l.add(2)
    assert(l.head != l.tail)
  end

  def test_get_head_by_index
    l = LinkedList.new
    l.add(1)
    assert_equal(1, l.get(0))
  end

  def test_index_vs_size
    l = LinkedList.new
    l.add(1)
    index = 0
    assert(l.size - index == 1)
  end

  def test_get_tail_by_index
    l = LinkedList.new
    l.add(1)
    l.add(2)
    assert_equal(2, l.get(1))
  end

  def test_get_raise_index_error
    l = LinkedList.new
    l.add(1)
    assert_raises(IndexError) { l.get(1) }
  end

  def test_get
    l = LinkedList.new
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    assert_equal(3, l.get(2))
    assert_equal(2, l.get(1))
    assert_equal(1, l.get(0))
    assert_equal(4, l.get(3))
  end

  def test_add_at_front_by_index
    l = LinkedList.new
    l.add(3)
    l.add_at(0, 5)
    assert_equal(5, l.head.key) # head is updated
    assert_equal(3, l.tail.key) # tail is updated
    assert_equal(2, l.size) # size is updated
  end

  def test_add_next_to_head_by_index
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.add_at(1, 4)
    assert_equal(4, l.get(1)) # successful insert
    assert_equal(3, l.head.key) # head remains
    assert_equal(5, l.tail.key) # tail remains
  end

  def test_add_in_middle_by_index
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.add(7)
    l.add(9)
    l.add_at(2, 6)
    assert_equal(6, l.get(2))
  end

  def test_add_at_index
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.add_at(1, 11)
    l.add_at(0, 13)
    assert_equal(11, l.get(2))
    assert_equal(5, l.get(3))
  end

  def test_remove_and_size_reduces
    l = LinkedList.new
    l.add(3)
    assert_equal(1, l.size)
    l.remove(0)
    assert_equal(0, l.size)
  end

  def test_remove_raise_index_error
    l = LinkedList.new
    l.add(3)
    assert_raises(IndexError) { l.remove(1) }
  end

  def test_remove_second_node
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.add(7)
    l.remove(1)
    assert_equal(7, l.head.next_pointer.key)
    assert_equal(l.tail.key, l.head.next_pointer.key)
  end

  def test_remove_head
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.remove(0)
    assert_equal(5, l.head.key)
    assert(l.head == l.tail)
  end

  def test_remove_tail
    l = LinkedList.new
    l.add(3)
    l.add(5)
    l.remove(1)
    assert_equal(3, l.head.key, 'Head does not match')
    assert_equal(3, l.tail.key, 'Tail does not match')
  end

  def test_add_at_index_in_empty_list
    l = LinkedList.new
    l.add_at(0, 8)
    assert_equal(8, l.get(0))
    assert(l.head == l.tail)
    assert_equal(1, l.size)
  end



end
