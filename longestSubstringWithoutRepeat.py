# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# problem 3 - Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i, mp = 0, 0, {}
        for j, ch in enumerate(s):
            if ch in mp:
                i = max(mp[ch], i)
            ans = max(ans, j - i + 1)
            mp[ch] = j + 1
        return ans
