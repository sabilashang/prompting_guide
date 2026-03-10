# Messy Fibonacci (no hints; for independent practice)
I have written a Python function that calculates the Fibonacci number using a while loop. 
Please improve the code while keeping the same iterative approach.

Requirements:
- Keep the logic iterative (do not use recursion).
- Make the code more Pythonic and readable.
- Add proper comments explaining each step.
- Add input validation.
- Follow good programming practices.
- Keep the algorithm efficient (O(n) time and O(1) space).

Here is my code:

def fib(n):
    a = 0
    b = 1
    c = None
    if n == 0:
        return 0
    if n < 0:
        return 'no'
    if n == 1:
        return 1
    k = 2
    while k <= n:
        c = a+b
        a = b
        b = c
        k = k+1
    return c

if __name__ == "__main__":
    print('fib 8 =', fib(8))

Please return the improved version and briefly explain the improvements.
