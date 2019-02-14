require 'minitest/autorun'
load './my_queue.rb'

class MyQueueTest < MiniTest::Test
  def test_init_return_queue_instance
    q = MyQueue.new
    assert_instance_of(MyQueue, q)
  end

  def test_init_returns_default_vars
    q = MyQueue.new
    assert_equal(0, q.size)
    assert_nil(q.head && q.tail)
  end

  def test_size_single_add
    q = MyQueue.new
    q.add(1)
    assert_equal(1, q.size)
    assert_equal(2, q.tail.key + q.head.key)
  end

  def test_head_tail_same_object
    q = MyQueue.new
    q.add(1)
    assert_same(q.head, q.tail)
  end

  def test_add_two_head_vs_tail
    q = MyQueue.new
    q.add(1)
    q.add(2)
    assert(q.head != q.tail)
  end

  def test_multiple_adds
    q = MyQueue.new
    q.add(1)
    q.add(3)
    q.add(5)
    q.add(7)
    assert_equal(4, q.size)
    assert_equal(7, q.tail.key)
    assert_equal(1, q.head.key)
  end

  def test_size_after_remove
    q = MyQueue.new
    q.add(1)
    q.remove
    assert_equal(0, q.size)
  end

  def test_remove_on_empty
    q = MyQueue.new
    assert_equal(-1, q.remove)
  end

  def test_remove_only_item
    q = MyQueue.new
    q.add(1)
    assert_equal(1, q.remove)
    assert_nil(q.head && q.tail)
  end

  def test_multiple_remove
    q = MyQueue.new
    q.add(1)
    q.add(3)
    q.add(5)
    q.add(7)
    assert_same(7, q.tail.key)
    assert_same(1, q.remove)
    assert_same(3, q.head.key)
    assert_same(3, q.remove)
    assert_same(5, q.head.key)
    assert_same(7, q.tail.key)
    assert_same(5, q.remove)
    assert_same(q.head, q.tail)
    assert_same(7, q.remove)
  end

  def test_multiple_adds_and_removes
    q = MyQueue.new
    q.add(3)
    assert_equal(3, q.remove)
    q.add(5)
    q.add(7)
    assert_equal(5, q.remove)
    assert_equal(7, q.remove)
  end

end