# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        res = 1
        left = 0
        for i in range(len(s)):
            if s[i] in s[left:i]:
                left += s[left:i].index(s[i])+1
            res = max(res, i - left+1)
        return res
