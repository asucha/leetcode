

# leetcode nickname asucha_473109

# 2026-08-16 leetcode daily problem --- solved
#   2029. Stone Game IX --- mid

# Topics:
# Game Theory, Math, Greedy, Minimax, Counting, Nim Game, Zero-sum Game

"""
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

Constraints:

1 <= stones.length <= 10^5
1 <= stones[i] <= 10^4
"""

from typing import List

# attempt 2:
class Solution:

    def stoneGameIX(self, stones: List[int]) -> bool:

        # "changing" the stone values into relevant 0, 1 or 2 and counting them
        counted = [0, 0, 0]
        for stone in stones:
            counted[stone % 3] += 1
                # sum(counted) is how many stones are left
                # (counted[1] + counted[2]*2)%3 is the the sum reminder or remaining stones

        if counted[0]%2 == 0:
            return counted[1] > 0 and counted[2] > 0
        else:
            return abs(counted[1] - counted[2]) > 2
