require 'minitest/autorun'
load './recursion.rb'

class RecursionTest < MiniTest::Test
  def test_sum_recursion_one
    assert_equal(10, sum(4))
  end

  def test_sum_recursion_two
    assert_equal(55, sum(10))
  end

  def test_factorial_recursion_one
    assert_equal(120, factorial(5))
  end

  def test_fibonacci_recursion_one
    assert_equal(8, fibonacci(6))
  end
end