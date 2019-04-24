require 'minitest/autorun'
load './backtracking_recursion.rb'

class BackTrackingRecursionTest < Minitest::Test
  def test_true
    assert(exact_sum?(12, [1, 2, 3, 4, 5]))
    assert(exact_sum?(201, [37, 42, 10, 23, 15, 25, 11, 6, 19, 25, 51]))
    assert(exact_sum?(50, [1, 3, 5, 37, 18, 5]))
  end
  def test_false
    assert_equal(false, exact_sum?(11, [1, 5, 9, 13]))
  end
end