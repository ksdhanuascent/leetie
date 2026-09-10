# ──────────────────────────────────────────────────
# Problem  : 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Tags     : Hash Table, String, Sliding Window
# Link     : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Runtime  : 306 ms (beats 54%)
# Memory   : 16444000 (beats 42%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            # If we have seen the character and its previous index is within the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer to the right of the duplicate's previous index
                left = char_map[s[right]] + 1
            
            # Update the character's most recent index
            char_map[s[right]] = right
            
            # Calculate the max length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length