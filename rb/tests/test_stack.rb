require 'minitest/autorun'
load './my_stack.rb'

class MyStackTest < MiniTest::Test
  def test_init_returns_class
    s = MyStack.new
    assert_instance_of(MyStack, s)
  end

  def test_init_vars_defaults
    s = MyStack.new
    assert_nil(s.head)
    assert_nil(s.min_stack)
    assert_equal(0, s.size)
  end

  def test_push
    s = MyStack.new
    s.push(3)
    s.push(5)
    assert_equal(2, s.size)
  end

  def test_push_and_head
    s = MyStack.new
    s.push(3)
    assert_equal(3, s.head.key)
    s.push(5)
    assert_equal(5, s.head.key)
    s.push(7)
    assert_equal(7, s.head.key)
    s.push(9)
    assert_equal(9, s.head.key)
  end

  def test_size_after_single_pop
    s = MyStack.new
    s.push(3)
    s.pop
    assert_equal(0, s.size)
  end

  def test_head_after_single_pop
    s = MyStack.new
    s.push(3)
    s.pop
    assert_nil(s.head)
  end

  def test_push_and_pop
    s = MyStack.new
    s.push(3)
    s.push(5)
    assert_equal(5, s.head.key)
    assert_equal(5, s.pop)
    assert_equal(3, s.head.key)
    assert_equal(1, s.size)
  end

  def test_multiple_push_and_pops
    s = MyStack.new
    s.push(3)
    s.push(5)
    s.push(10)
    assert_equal(10, s.head.key)
    assert_equal(10, s.pop)
    assert_equal(5, s.head.key)
    assert_equal(5, s.pop)
    assert_equal(3, s.head.key)
    assert_equal(3, s.pop)
    assert_equal(0, s.size)
  end

  def test_pop_on_empty_return_nil
    s = MyStack.new
    assert_nil(s.pop)
  end

  def test_top
    s = MyStack.new
    s.push(3)
    s.push(5)
    assert_equal(5, s.top)
  end

  def test_top_on_empty_return_nil
    s = MyStack.new
    assert_nil(s.top)
  end

  def test_min_exists
    s = MyStack.new
    assert_equal(true, s.public_methods.include?(:min))
  end

  def test_min_updates_after_push
    s = MyStack.new
    s.push(3)
    assert_equal(3, s.min)
    s.push(2)
    assert_equal(2, s.min)
    s.push(1)
    assert_equal(1, s.min)
  end

  def test_min_updates_after_pop
    # min needs next pointer to keep sequence of sorting from min to max
    s = MyStack.new
    s.push(3)
    s.push(2)
    s.push(1)
    assert_equal(1, s.min)
    s.pop
    assert_equal(2, s.min)
    s.pop
  end

  def test_min_after_multiple_pops
    s = MyStack.new
    s.push(3)
    s.push(2)
    s.push(1)
    s.pop
    s.pop
    assert_equal(3, s.min)
  end

  def test_min_intercalation
    s = MyStack.new
    s.push(10) # 9
    s.push(20) # 8
    s.push(5) # 7
    s.push(30) # 6
    s.push(3) # 5
    s.push(40) # 4
    s.push(1) # 3
    s.push(50) # 2
    s.push(70) # 1
    s.pop # 1
    s.pop # 2
    assert_equal(1, s.min)
    s.pop # 3
    assert_equal(3, s.min)
    s.pop # 4
    assert_equal(3, s.min)
    s.pop # 5
    assert_equal(5, s.min)
    s.pop # 6
    assert_equal(5, s.min)
    s.pop # 7
    assert_equal(10, s.min)
    s.pop # 8
    assert_equal(10, s.min)
    s.pop # 9
    assert_nil(s.min)
  end
end
