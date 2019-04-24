def move(starting, goal)
  case starting
  when 1
    if goal == 3
      "#{starting}->#{2} #{starting}->#{3} #{2}->#{3}"
    elsif goal == 2
      "#{starting}->#{3} #{starting}->#{2} #{3}->#{2}"
    end
  when 2
    if goal == 3
      "#{starting}->#{1} #{starting}->#{3} #{1}->#{3}"
    elsif goal == 1
      "#{starting}->#{3} #{starting}->#{1} #{3}->#{1}"
    end
  else
    'Not allowed, sorry'
  end
end

def hanoi_steps(discs_in_peg_1)
end

