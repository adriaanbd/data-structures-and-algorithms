def exact_sum?(target, coins)
  # puts "Weights: #{coins}\n"
  subset_sum?(target, coins, 0)
end

def subset_sum?(sum, weights, n)
  # puts "Sum: #{sum}, n: #{n}, Weights[#{n} + 1] = #{weights[n + 1]}\n"
  return true if sum == 0

  return false if n == weights.length - 1 && sum != 0

  return subset_sum?(sum, weights, n + 1) if weights[n + 1] > sum

  subset_sum?(sum, weights, n + 1) || subset_sum?(sum - weights[n + 1], weights, n + 1)
end

# Other solution:

=begin
 
def exact_sum?(k, coins)
  return true if k == 0
  return false if coins.empty? || k < 0
  
  exact_sum?(k-coins[0], coins[1..-1]) || exact_sum?(k, coins[1..-1])
end
  
=end
