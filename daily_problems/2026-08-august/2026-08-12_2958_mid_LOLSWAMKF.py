
# leetcode nickname asucha_473109

# 2026-08-12 leetcode daily problem --- mid --- 2958. Length of Longest Subarray With at Most K Frequency --- solved

"""
You are given an integer array nums and an integer k.
The frequency of an element x is the number of times it occurs in an array.
An array is called good if the frequency of each element in this array is less than or equal to k.
Return the length of the longest good subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.
"""

# first attempt - failes

from typing import List

# class Solution:
#     def maxSubarrayLength(self, nums: List[int], k: int) -> int:
#         if len(nums) > 1:
#             longest = len(nums)
#             frequencies = {i: nums.count(i) for i in nums}
#             popElementIndex = 0 if nums[0] == nums[1] else -1
#             while longest > 1:
#                 if max(frequencies.values()) <= k:
#                     return longest
#                 if frequencies[ nums[popElementIndex] ] == 1:
#                     del frequencies[ nums[popElementIndex] ]
#                 else:
#                     frequencies[ nums[popElementIndex] ] -= 1
#                 longest -= 1
#                 popElementIndex = 0 if nums[0] == nums[1] else -1
#         return 1


# second attempt - changing the approach from chosing head/tail shrinkage,
# to expanding on head and shrinking on tail


from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        frequencies = defaultdict(int)
        longest = 0
        tail = 0

        for head in range(len(nums)):
            frequencies[nums[head]] += 1
            while frequencies[nums[head]] > k:
                frequencies[nums[tail]] -= 1
                tail += 1
            longest = max(longest, head-tail+1)
        return longest
