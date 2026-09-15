# ──────────────────────────────────────────────────
# Problem  : 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Tags     : Two Pointers, String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm, Boyer–Moore String-Search Algorithm
# Link     : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12400000 (beats 82%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len = len(haystack)
        n_len = len(needle)
        
        # Iterate through the haystack up to the point where the remaining 
        # characters are at least the length of the needle
        for i in range(h_len - n_len + 1):
            # Check if the current substring matches the needle
            if haystack[i:i + n_len] == needle:
                return i
                
        # If no match is found after checking all possibilities
        return -1