require 'minitest/autorun'
load './sqrt_binary_search.rb'

class SqrtBinarySearchTest < MiniTest::Test
  def test_one
    assert_equal(5, sqrt(25))
  end

  def test_two
    assert_equal(84, sqrt(7056))
  end
end