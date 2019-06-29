=begin
A duplicate is a number whose value appeared earlier in the list. Given a list of numbers, return an array with all the duplicates in the order that they appear. (Duplicates that appear multiple times should be printed multiple times).

Use Ruby's Set class to solve the challenge.
=end

def find_duplicates(array)
  s = Set.new 
  array.reject { |item| s.add?(item) }
end

p find_duplicates([1, 2, 3, 1, 5, 6, 7, 8, 5, 2])
# => [1, 5, 2]

p find_duplicates([3, 501, 17, 23, -43, 67, 5, 888, -402, 235, 77, 99, 311, 1, -43])
# => [-43]

# model solution after submission:

=begin 

def find_duplicates(array)
  set = Set.new
  duplicates = []
  
  array.each do |element|
    if set.include?(element)
      duplicates << element
    else
      set.add(element)
    end
  end
  
  duplicates
end

=end