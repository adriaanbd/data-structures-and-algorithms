def get_brackets(string)
  open = '(', '[', '{'
  close = ')', ']', '}'
  brackets = []
  string.each_char do |char|
    brackets.push(char) if open.include?(char) || close.include?(char)
  end
  brackets
end

def balanced_brackets?(string)
  open = '(', '[', '{'
  close = ')', ']', '}'
  stack = []
  get_brackets(string).each do |char|
    if open.include?(char)
      stack.push(char)
    else
      false if stack.empty?
      top = stack.pop
      return false if top == open[0] && char != close[0] || top == open[1] && char != close[1] || top == open[2] && char != close[2]

    end
  end
  stack.empty?
end
