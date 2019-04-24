def sqrt(number)
  sqrt_recursive(number, 0, number)
end

def sqrt_recursive(number, min_interval, max_interval)
  arr = (min_interval..max_interval).to_a
  mid_idx = arr.length / 2
  mid_val = arr[mid_idx]
  answer = mid_val * mid_val
  return mid_val if answer == number

  if answer > number
    sqrt_recursive(number, min_interval, arr[mid_idx - 1])
  else
    sqrt_recursive(number, arr[mid_idx + 1], arr[-1])
  end
end