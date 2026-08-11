
# leetcode nickname asucha_473109

# 2026-08-11 leetcode daily problem --- easy --- 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum --- solved

from typing import List

class Solution:

    def missingInteger(self, nums: List[int]) -> int:

        # aggregating the sum of the longest sequential prefix
        prefixSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefixSum += nums[i]
            else:
                break

        # finding smallest integer not included in nums that is GE the sum calculated earlier
        while True:
            if prefixSum not in nums:
                return prefixSum    # fin
            else:
                prefixSum += 1
