
# leetcode nickname asucha_473109

# 2026-08-06 leetcode daily problem --- easy --- 3345. Smallest Divisible Digit Product I --- solved

"""
You are given two integers n and t.
Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
"""

# just took advantage of casting and recasting int into string and aggregating over each character

from math import prod

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if prod( int(d) for d in str(n) ) % t == 0:
                return n
            n += 1
