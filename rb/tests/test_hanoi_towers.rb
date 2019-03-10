require 'minitest/autorun'
load './hanoi_towers.rb'

class HanoiTowersEzTest < MiniTest::Test
  def test_one
    assert_equal("1->2 1->3 2->3", move(1, 3))
    assert_equal("2->1 2->3 1->3", move(2, 3))
  end
end