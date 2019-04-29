require 'minitest/autorun'
load '../trees-and-graphs/connected_components.rb'

class ConnectedGraphTest < Minitest::Test
  def test_all_values_connected_1
    graph = { 0 => [2],
              1 => [4],
              2 => [0, 5, 3],
              3 => [5, 2],
              4 => [5, 1],
              5 => [4, 2, 3] }
    assert(connected_graph?(graph))
  end

  def test_all_values_connected_2
    graph = { 0 => [1, 2],
              1 => [0, 2],
              2 => [0, 1, 3, 4, 5],
              3 => [2, 4],
              4 => [3, 2],
              5 => [2] }
    assert(connected_graph?(graph))
  end
end