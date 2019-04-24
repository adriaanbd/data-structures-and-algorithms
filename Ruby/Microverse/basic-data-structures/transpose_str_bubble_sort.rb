def transpose(string)
  case_array = string.split('')
  finish_point = case_array.length - 2

  (case_array.length - 1).times do
    for i in 0.upto(finish_point) do
      if case_array[i] == 'g' && case_array[i + 1] == 'n'
      case_array[i], case_array[i + 1] = case_array[i + 1], case_array[i]
      end
    end
    finish_point -= 1
  end
  case_array.join('')
end

string = 'rignadingdiggn!'
puts transpose(string)