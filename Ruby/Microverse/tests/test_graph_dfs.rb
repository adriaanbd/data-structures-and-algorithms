require "minitest/autorun"
load "./graph_dfs.rb"

class GraphDFSTest < Minitest::Test
  def test_graph_default
    graph = {
      0 => [2], 
      1 => [4], 
      2 => [5, 0, 3], 
      3 => [2], 
      4 => [1, 5], 
      5 => [4, 2]
    }
    assert_equal([0, 2, 5, 4, 1, 3], depth_first_search(graph))
  end

  def test_graph_6_nodes
    graph = {
      0=>[1, 2], 
      1=>[0, 2], 
      2=>[0, 1, 3, 4, 5], 
      3=>[2, 4], 
      4=>[3, 2], 
      5=>[2]
    }
    assert_equal(graph.keys, depth_first_search(graph))
  end

  def test_graph_7_nodes
    graph = {
      0=>[1, 2],
      1=>[0, 3, 4],
      2=>[0, 5, 6],
      3=>[1],
      4=>[1, 5],
      5=>[2, 4],
      6=>[2]
    }
    assert_equal([0, 1, 3, 4, 5, 2, 6], depth_first_search(graph))
  end
end
