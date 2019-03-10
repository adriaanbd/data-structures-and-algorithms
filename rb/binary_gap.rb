# CODILITY
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

# Problem Statement
#
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N. 
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
#
# Write a function:
#
# def solution(n) that, given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.


# Second try:

def solution(n, gaps = [])
  n = n.to_s(2).split('') unless n.is_a?(Array)
  idx = n.index('1')
  subarr = n[idx + 1..-1]
  gap = subarr.index('1')
  gaps << gap unless gap.nil?
  solution(subarr, gaps) unless subarr.empty? || subarr.length == 1 || gap.nil?
  gaps.nil? || gaps.empty? ? 0 : gaps.max
end

# First try:

# def solution(n)
#   bin = n.to_s(2)
#   count = 0
#   limit_count = 0
#   count_ary = []
#   bin.each_char do |i|
#     if i == '1'
#       limit_count += 1
#     elsif limit_count == 2
#       count_ary << count
#       count = 0
#     elsif i == '0'
#       count += 1
#     end
#   end
#   max_count = count_ary.max
#   max_count.nil? ? 0 : max_count
# end

