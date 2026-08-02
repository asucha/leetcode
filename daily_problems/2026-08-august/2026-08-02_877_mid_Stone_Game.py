
# leetcode nickname asucha_473109

# 2026-08-02 leetcode daily problem --- medium --- 877. Stone Game --- solved

"""

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.


Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example 2:

Input: piles = [3,7,2,3]
Output: true

"""

# My reasoning:

# First attempt
#
# Since both Alice and Bob are playing optimally, the game winner depends solely on whose turn is first
# and what is the stones' setting. The players work like the queue mechanism taking the greater out of
# the two ends. The direction of the flow is only one way, threfore it could be a good place to treat this
# problem as the Directed Acyclic Graph, altho I shall try the non-recursive approach first.
# The pile must be rearranged to the array of the pairs made of head and tail of the remaining piles, where
# first of the pair is greater or equal to the second one. Then the sum of odd or even indices in the "sorted"
# array will be the returning True of False. It is important to also consider what stone piles remain after
# pulling one, since we want to ma the nest choice with the smallest possible max() number of the two.

from typing import List

# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:

#         order = []

#         while len(piles) > 0:
#             if piles[0] == piles[-1] and len(piles) > 1:
#                 order.append( piles.pop(0) if piles[1] <= piles[-2] else piles.pop(-1) )
#             else:
#                 order.append( piles.pop(0) if piles[0] >= piles[-1] else piles.pop(-1) )

#         return sum(order[::2]) > sum(order[1::2])

# This attempt worked for most of the cases but only included the "one level deep comparison" and hasn't
# incorporated the mechanism of sacrificing some moves for the more valuable reward later on.
# Flipping the problem on it's head my popping the piles from the middle also would not work,
# since "the middle" in question is not a stationary (e.g floor(len/2)) index, and it's location depends
# on the agreggated summary cost of all the moves
# Therefore the Graph approach it is...


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        n = len(piles)

        @lru_cache(None)
        def helper(i, j):

            if i > j:
                return 0

            whichPlayer = (j-i-n) % 2
            if whichPlayer == 1:  # here checking first player of the two in the given smaller interval
                return max( helper(i+1, j) + piles[i], helper(i, j-1) + piles[j] )
            else:
                return min( helper(i+1, j) - piles[i], helper(i, j-1) - piles[j] )

        return helper(0, n-1) > 0


test = Solution()
print(test.stoneGame([3,7,2,3]))
