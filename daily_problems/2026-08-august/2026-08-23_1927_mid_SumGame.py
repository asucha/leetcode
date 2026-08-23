
# leetcode nickname asucha_473109

# 2026-08-23 leetcode daily problem --- solved
#   1927. Sum Game --- mid

# Topics:
# Math, Game Theory

"""
Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

1. Choose an index i where num[i] == '?'.
2. Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

- For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.
"""

# My solution:

# the same number of wildcards ("?"s) on both sides cancel out since players
# can place optimally any of 0-9 digits on each side therefore the difference
# between number of wildcards. Each wildcard has the potential of being 0-9,

class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        left = num[: n//2]
        right = num[n//2 :]

        wildcardL = left.count("?")
        wildcardR = right.count("?")

        # if the n of wildcards is odd, the last move is Alice's
        # therefore she wins since she has the final say
        if (wildcardL + wildcardR) %2 != 0:
            return True

        # here Bob wins only if sums on both sides can be balanced
        # by net wildcards
        else:
            sumL = sum( [int(d) for d in left if d != "?"] )
            sumR = sum( [int(d) for d in right if d != "?"] )

            return float(sumL - sumR) != (wildcardR - wildcardL) * 4.5
