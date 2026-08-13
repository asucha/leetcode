
# leetcode nickname asucha_473109

# 3. Longest Substring Without Repeating Characters --- solved

# Topics: Hash Table, Sliding Window


"""
Given a string s, find the length of the longest substring without duplicate characters.
"""


# First attempt - without using hashtable

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest = 0
        for c in s:
            if c in substring:
                substring = substring[substring.find(c)+1::]
            substring += c
            if len(substring) > longest:
                longest = len(substring)
        return longest

testString = "abcabcbb"
test = Solution()
print(test.lengthOfLongestSubstring(testString))
