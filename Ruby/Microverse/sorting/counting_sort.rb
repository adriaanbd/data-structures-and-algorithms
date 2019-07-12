=begin 
You will be given a list that contains both integers and strings. Can you print the strings in order of their accompanying integers? If the integers for two strings are equal, make sure to print them in the order they appeared in the original list.
=end

def full_counting_sort(array)
  counts = count_array(array)
  answer = []
  counts.each_with_index do |item, idx|
    unless item.nil?
      item.each { |position| answer << array[position].split[1] }
    end
  end
  answer
end

def count_array(array)
  counts = Array.new(1000, nil)
  array.each_with_index do |item, idx| 
    position = item.split[0].to_i
    if counts[position].nil?
      counts[position] = [idx]
    else
      counts[position] << idx 
    end
  end
  counts
end

p full_counting_sort(["0 ab", "6 cd", "0 ef", "6 gh", "4 ij", "0 ab", "6 cd", "0 ef", "6 gh", "0 ij", "4 that", "3 be", "0 to", "1 be", "5 question", "1 or", "2 not", "4 is", "2 to", "4 the"])
# => ["ab", "ef", "ab", "ef", "ij", "to", "be", "or", "not", "to", "be", "ij", "that", "is", "the", "question", "cd", "gh", "cd", "gh"]