
# leetcode nickname asucha_473109

# 2026-08-14 leetcode daily problem --- easy --- 3090. Maximum Length Substring With Two Occurrences --- solved

# Topics:
# Hash table, Sliding Window

"""
Given a string s, return the maximum length of a substring such that it contains
at most two occurrences of each character.
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        substring = ""
        longest = 0
        for c in s:
            if substring.count(c) == 2:
                substring = substring[substring.find(c)+1::]
            substring += c
            if len(substring) > longest:
                longest = len(substring)
        return longest
