# ──────────────────────────────────────────────────
# Problem  : 5. Longest Palindromic Substring
# Difficulty: Medium
# Tags     : Two Pointers, String, Dynamic Programming, Manacher
# Link     : https://leetcode.com/problems/longest-palindromic-substring/
# Runtime  : 353 ms (beats 67%)
# Memory   : 12324000 (beats 86%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
            
        start, end = 0, 0
        
        # Helper function to find the bounds of the palindrome around a center
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid bounds (stepping back one from the failing condition)
            return left + 1, right - 1
            
        for i in range(len(s)):
            # Odd length palindromes (centered on a single character)
            left1, right1 = expandAroundCenter(i, i)
            # Even length palindromes (centered between two characters)
            left2, right2 = expandAroundCenter(i, i + 1)
            
            # Update the maximum palindrome bounds found so far
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
                
        return s[start:end + 1]