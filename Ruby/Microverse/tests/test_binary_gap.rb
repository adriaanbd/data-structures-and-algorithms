require 'minitest/autorun'
load './binary_gap.rb'

class BinaryGapTest < MiniTest::Test
  def test_3
  	assert_equal(3, solution(17))
  end
  def test_10 
  	assert_equal(1, solution(10))
  end
  def test_7
  	assert_equal(0, solution(7))
  end
  def test_32
  	assert_equal(0, solution(32))
  end
end
