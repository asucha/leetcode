

# leetcode nickname asucha_473109

# 2026-08-22 leetcode daily problem --- solved
#   3622. Check Divisibility by Digit Sum and Product --- easy

# Topics:
# Math

"""
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

- The digit sum of n (the sum of its digits).
- The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.
"""

# oneliner solution

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        return n % ( sum([int(d) for d in str(n)]) + prod([int(d) for d in str(n)])) == 0
