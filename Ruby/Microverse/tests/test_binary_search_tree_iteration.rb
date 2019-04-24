require 'minitest/autorun'
load './binary_search_tree_iteration.rb'

class MyBstIterationTest < MiniTest::Test
  def test_one
    assert_equal(3, tree_height([2, 7, 5, 2, 6, 0, 9]))
  end

  def test_two
    assert_equal(4, tree_height([1, 7, 5, 2, 6, 0, 9, 3, 7, 5, 11, 0, 0, 4, 0]))
  end

  def test_three
    assert_equal(4, tree_height([5, 3, 2, 9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 5, 0]))
  end
end