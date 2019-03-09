def solution(n)
  bin = n.to_s(2)
  count = 0
  limit_count = 0
  count_ary = []
  bin.each_char do |i|
    if i == '1'
      limit_count += 1
    elsif limit_count == 2
      count_ary << count
      count = 0
    elsif i == '0'
      count += 1
    end
  end
  max_count = count_ary.max
  max_count.nil? ? 0 : max_count
end