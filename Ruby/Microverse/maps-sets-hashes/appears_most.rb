=begin 

A Map is also known as a Dictionary, since it can be used to store items in a similar manner as a dictionary, where each word maps to a specific definition. 

These are the basic methods of a Map:

    [key] = value - Adds the key and value to the map, so they are now associated with each other. If this key was already in the Map, it will now point to the new value only.
    [key] - Returns the value that the key maps to.
    delete(key) - Removes the key-value mapping of this key from the map.
    has_key?(key) - This returns true if the key is in the map and false otherwise (like the contains method of Set).

Map in Ruby
Ruby standard library has the class Hash.
https://ruby-doc.org/core/Hash.html

Return the number in each list that appears the most times.

=end

def appears_most_times(array)
  counts = Hash.new
  max = array.first
  array.each do |item|
    if counts[item].nil?
      counts[item] = 1 
    else
      counts[item] += 1
      max = item if counts[item] > counts[max]
    end
  end
  max
end

# model solution:

=begin
def appears_most_times(array)
  # write your code here
  counts = Hash.new(0)
  
  array.each do |element|
    counts[element] += 1
  end
  
  counts.max_by { |k, v| v }&.first
end
=end

puts appears_most_times([1, 2, 3, 1, 5])
# => 1

puts appears_most_times([23, 43, 67, 88, 42, 35, 77, 88, 99, 11])
# => 88

puts appears_most_times([4376, -345, -345, 4376, -345, 84945, 4376, -345, -26509, 4376, 84945, 84945, -26509, 896341, 4376])
# => 4376