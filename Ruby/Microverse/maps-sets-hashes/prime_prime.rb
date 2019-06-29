=begin
Challenge
The "Prime Prime" is a prime number that is the factor of the most numbers in a given list. Can you find the Prime prime in each list?
For example, for the list {2, 3, 5, 6, 9}, the answer is 3, since 3 is a factor of 3, 6, and 9, which is more than any other number in the list.
Note: Each number N in a list will be in the range 2 to 10,000.
=end

def prime_prime(array)
  primes = arr_of_primes(array)
  h = {}
  max = 0
  primes.each do |i| 
    count = 0
    array.each do |j| 
      r = j % i
      if r.zero?
        count += 1
      end
    end
    h[i] = count
  end
  h.key(h.values.max)
end

def arr_of_primes(arr)
    m = 2
    n = arr.max
    
    candidates = [*m..n]
    idx = 0 
    primes = [] 
    val = candidates[0]
    
    while val**2 <= (candidates.max) do
        primes << candidates.shift
        candidates = candidates.reject { |i| i % val == 0}
        val = candidates[0]
    end
    primes = primes + candidates
    primes
end

p prime_prime([2, 3, 5, 6, 9])
# => 3

puts prime_prime([121, 17, 21, 29, 11, 341, 407, 19, 119, 352])
# # => 11

puts prime_prime([7, 6, 7, 3, 77, 14, 28, 35, 42])
# # => 7