def sum(number)
  number.zero? ? number : number + sum(number - 1)
end

def factorial(n)
  n.zero? ? 1 : n * factorial(n - 1)
end

def fibonacci(n)
  n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2)
end