require 'minitest/autorun'
load './graph_bfs.rb'

class GraphBFSTest < Minitest::Test
  def test_toy_graph
    hash = { 
      0 => [2], 
      1 => [4], 
      2 => [5, 0, 3], 
      3 => [2], 
      4 => [1, 5], 
      5 => [4, 2]
    }
    assert_equal([0, 2, 5, 4], graph(hash))
  end
end