# Efficiency

The efficiency or complexity of a program depends on the **time** it will take to *run* it **and** the amount of **space** the program will require in the computer's *memory*. There is often a trade-off between the two, by selecting a data structure that takes more space but takes less time to run. In other words, the efficiency of a program is determined by how well the program uses the computer's resources to get something done.

## Algorithms

An algorithm is a series of steps for solving a problem. It takes some kind of input and then produces some kind of desired output. Since an algorithm is a solution to a problem, there are usually many different algorithms to the same problem, but some will be more efficient than others.

Generally speaking, as the input to an algorithm increases, the time required to run the algorithm may also increase.

### Linear vs Quadratic time

#### Linear
A larger input size will increase the number operations executed by a rate proportional to the input size, i.e. 1-to-1 or 2-to-2.

#### Quadratic
A larger input size will increase the number of operations executed by the square of the input size, i.e. 2-to-4 or 4-to-16.

### Big O Notation

#### Basics

The O in Big O stands for the *order* of a function or algorithm, as in the *rate of increase* in the run-time of an algorithm, in terms of the input size *n*.

For example, let's take into consideration the following code:

```pseudocode
function decode(message)
    create output string
    for each letter in input
    	get new_letter from letter location in cipher
    	add new_letter to output
    return output
```

* The `create` and `return` only happen once:  O( 2)
* Both lines inside the for loop run twice for each letter in the input: O(2n+2)
* If our input size is 10: `2(10) + 2 = 22`. To get the actual efficiency, you can multiply 22 by the amount of times it takes the computer to run one line of code.
* If our input size is 1 million: `2(1000000) + 2 = 2 million`

Another example:

```python
def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")
```

Since there are two for loops, one being nested inside the other, the big O notation for this function would be `n**2`.

#### Other considerations

Another look at the following function:

```pseudocode
function decode(message)
    create output string
    for each letter in input
    	get new_letter from letter location in cipher
    	add new_letter to output
    return output
```

Some considerations:

* Does the for loop itself count for something?

* In order for the loop to work, a computation needs to be executed to get the next letter in the string. Since it happens one time for every input letter, we can just add 1 to the value before n: O(3n + 2)

* It's really hard to predict exactly how many computations the above-mentioned pseudo-code will take.

* The `get new_letter from letter location in cipher` could take a different number of computations based on the data structure the cipher is using. If we're storing the data in a list and we're checking each letter against the current letter in order to solve the code, it could be as many as 26 checks for each letter in the input string: O(36n + 2).

* This is how it'd look like for two different input sizes:

  |    Case A    |      Case B       |
  | :----------: | :---------------: |
  |    n = 10    |   n = 1 million   |
  | O(29*10 + 2) | O(29*1000000 + 2) |
  |    O(292)    |    O(29000002)    |

#### Approximation

You may have noticed that the 2 in the O(2n + 2) has very little impact in the total efficiency, especially as the input size gets larger and larger. Because of this, approximation calculations are preferred, thus making the above calculation relevant only as O(n). 

The concept to grasp here is that some number of computations must be performed for each letter in the input.

### Resources

Big O Time Complexity Cheat Sheet:

http://bigocheatsheet.com/