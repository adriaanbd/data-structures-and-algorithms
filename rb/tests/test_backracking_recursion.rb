require 'minitest/autorun'
load './backtracking_recursion.rb'

class BackTrackingRecursionTest < Minitest::Test
  def test_true
    assert(exact_sum?(12, [1, 2, 3, 4, 5]))
  end
  def test_false
    assert_equal(false, exact_sum?(11, [1, 5, 9, 13]))
  end
end