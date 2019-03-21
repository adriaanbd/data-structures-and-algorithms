# Challenges

## Rooms Required

This problem was asked by Snapchat

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

## Perfect Square

This week's function, is_perfect_square, accepts a number and returns True if it's a perfect square and False if it's not. A perfect square is any number which has an integer square root. So 25 is a perfect square but 24 is not, 9 is a perfect square but 8 is not, 100 is a perfect square but 1000 is not.


Here's an example:

```
>>> is_perfect_square(64)
True
>>> is_perfect_square(65)
False
>>> is_perfect_square(100)
True
>>> is_perfect_square(1000)
False
```

Make sure that this function raises a TypeError when an invalid type is given (integers and floats are fine but strings aren't) and I want you to make sure your function works with sensible alternative numeric types like decimal.

The first bonus is to make sure your function returns False for negative numbers.

```
>>> is_perfect_square(-1)
False
>>> is_perfect_square(-4)
False
```

The second bonus is to make sure your function works for really big numbers.

```
>>> is_perfect_square(4624000000000000)
True
>>> is_perfect_square(4623999999999999)
False
```

The third bonus is to make your function accept an optional "complex" keyword-only argument which will allow your function to check whether the given number is a perfect square in the complex number system.

```
>>> is_perfect_square(-4, complex=True)
True
>>> is_perfect_square(-5, complex=False)
False
>>> is_perfect_square(512j, complex=True)
True
```

To be a complex perfect square, the complex square root of the number must have integers for both its real part and its imaginary part.

## Backtracking Recursion

You will be given a list of numbers where the first number is the desired sum and the remaining numbers are the coins. Determine if the coins can be added together to reach the exact sum. You cannot use the same coin twice, but you can use duplicate coins (if there are any).
For example, when given `(12, [1, 2, 3, 4, 5])`, print `true` since `1 + 2 + 4 + 5 = 12` (among other possibilities). When given `(11, [1, 5, 9, 13])`, print `false`, since there's no way to reach a sum of `11` with those numbers.

1. Go through the array of `coins` in order.
2. For each coin you reach, you can  either add it to your sum, or ignore it.
3. Try each of these possibilities, and go on to the next coin within each one of them.
4. Then repeat the same process with the next coin.

#### Converting it to code

The algorithm described above could not be encoded with a simple loop. This is because it **"splits in two" each time** to try out *every  possibility*, while a loop just goes through things *in order*.

The function should go through the array one number at a time, and **recursively call itself twice**: *Once, with the coin* subtracted from the desired sum, and once *without the coin*.

The beginning of the function should:
1. check if the end of the array has been reached, and
2. check if the sum is down to 0 or not.

#### Challenge

Given a number `k` and a list of `coins`, determine if the coins can be added together to equal k. Print `true` if you can get the exact sum and `false` otherwise.

Example

```
exact_sum?(12, [1, 2, 3, 4, 5])
=> true
```
```
exact_sum?(11, [1, 5, 9, 13])
=> false
```
