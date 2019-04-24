require 'minitest/autorun'
load './rotating_array.rb'

class RotatingArrayTest < MiniTest::Test
  def test_all_same
    assert_equal([1, 1, 1, 1], solution([1, 1, 1, 1], 1))
  end
  def test_all_diff
    assert_equal([9, 7, 6, 3, 8], solution([3, 8, 9, 7, 6], 3))
  end
  def test_rotations_eq_length
    assert_equal([1, 2, 3, 4], solution([1, 2, 3, 4], 4))
  end
  def test_empty
    assert_equal([], solution([], 4))
  end
end