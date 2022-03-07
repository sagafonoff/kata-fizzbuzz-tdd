# using pytest
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which
# are multiples of both three and five print “FizzBuzz “.
#
from fizzbuzz import fizzbuzz


def test_fizzbuzz_returns_number():
    assert fizzbuzz(1) == 1, "Should be 1"

def test_returns_fizz_when_number_divisible_by_three():
    assert fizzbuzz(3) == "Fizz", "Should be Fizz"

# Sample output:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# ... etc up to 100