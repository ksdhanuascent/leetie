# ──────────────────────────────────────────────────
# Problem  : 9. Palindrome Number
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/palindrome-number/
# Runtime  : 15 ms (beats 36%)
# Memory   : 12492000 (beats 19%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers cannot be palindromes (e.g., -121 reversed is 121-)
        if x < 0:
            return False
            
        original = x
        reversed_num = 0
        
        # Mathematically reverse the integer
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
            
        # Check if the reversed number is the same as the original
        return original == reversed_num