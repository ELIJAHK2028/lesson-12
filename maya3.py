"""
Understand:
Write a function to check if a number is even.
Edge Cases: Negative numbers and zero

Clues:
We can use % to check the divisibilty by 2
if n % 2 == 0, then the number is even.
if n % 2 != 0, then the number is odd.

Assemble:
Define a function that takes an integer n as input.
Check if n is divisible by 2 using the modulus operator.
If n % 2 == 0, return True
Otherwise, return False

"""

def is_even(n):
    return n % 2 == 0

print(is_even(4))
print(is_even(5))
print(is_even(6))
print(is_even(7))

