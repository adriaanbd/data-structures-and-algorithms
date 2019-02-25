require 'minitest/autorun'
load './transpose_str_linked_list.rb'

class TransposeStrTest < MiniTest::Test
  def test_init_returns_instance
    ng = NgLinkedList.new
    assert_instance_of(NgLinkedList, ng)
  end

  def test_init_returns_defaults
    ng = NgLinkedList.new
    assert_nil(ng.head)
    assert_equal(0, ng.size)
  end

  def test_push_updates_size
    ng = NgLinkedList.new
    ng.push('a')
    assert_equal(1, ng.size)
  end

  def test_push_g_update_head_tail
    ng = NgLinkedList.new
    ng.push('g')
    assert_equal('g', ng.head.key)
    assert_equal('g', ng.tail.key)
  end

  def test_push_gn_update_order
    ng = NgLinkedList.new
    ng.push('g')
    ng.push('n')
    assert_equal('g', ng.head.key)
    assert_equal('n', ng.tail.key)
  end

  def test_push_gng
    ng = NgLinkedList.new
    ng.push('g')
    ng.push('n')
    ng.push('g')
    assert_equal('g', ng.head.key)
    assert_equal('n', ng.tail.key)
    assert_equal('g', ng.tail.next_pointer.key)
    assert(ng.tail.next_pointer != ng.head)
  end

  def test_push_gngn
    ng = NgLinkedList.new
    ng.push('g')
    ng.push('n')
    ng.push('g')
    ng.push('n')
    assert_equal('n', ng.tail.key)
    assert_equal('n', ng.tail.next_pointer.key)
    assert(ng.tail != ng.tail.next_pointer)
    assert_equal('g', ng.tail.next_pointer.next_pointer.key)
    assert_equal('g', ng.head.key)
    assert(ng.head != ng.tail.next_pointer.next_pointer)
  end

  def test_push_multiple_chars
    ng = NgLinkedList.new
    ng.push('s')
    ng.push('i')
    ng.push('g')
    ng.push('n')
    assert_equal('s', ng.tail.key)
    assert_equal('g', ng.head.key)
    assert_equal('s', ng.tail.next_pointer.key)
  end

end