### Solution

We see the following description when we access to the server.

"""

We define a^^b to be such that a^^0 = 1 and a^^b = a^(a^^(b-1)), where x^y represents x to the power of y.
Given this, find a positive integer x such that a^^x = b mod p.

"""

Creating a function to solve this challenge is not diffucult, but if we simply do it, we'll fail, since it takes numerous time.
Therefore, we need to think of an efficient way. 

After some time thinking, I came up with a way of solving it using Euler's theorem shown in the [solver.py](./solver.py).


