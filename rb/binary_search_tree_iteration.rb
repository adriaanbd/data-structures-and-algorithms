def tree_height(tree_as_list)
  heights = [] # array to store heights of each sub tree
  (tree_as_list.length - 1).downto(0) do |i| # iterate from last element
    initial_height = tree_as_list[i].zero? ? 0 : 1
    left_child_idx = tree_as_list[2 * i + 1].nil? ? nil : heights.length - i - 1
    left_child_height = left_child_idx.nil? ? 0 : heights[left_child_idx]
    right_child_idx = tree_as_list[2 * i + 2].nil? ? nil : left_child_idx - 1
    right_child_height = right_child_idx.nil? ? 0 : heights[right_child_idx]
    total_height = initial_height + [left_child_height, right_child_height].max
    heights.push(total_height)
  end
  heights[-1]
end

tree_height([2, 7, 5, 2, 6, 0, 9])