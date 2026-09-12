# ──────────────────────────────────────────────────
# Problem  : 7. Reverse Integer
# Difficulty: Medium
# Tags     : Math
# Link     : https://leetcode.com/problems/reverse-integer/
# Runtime  : 12 ms (beats 89%)
# Memory   : 12348000 (beats 52%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def reverse(self, x):
        # Define the 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of the integer
        sign = -1 if x < 0 else 1
        
        # Convert absolute value to string, reverse it, and convert back to int
        reversed_x = int(str(abs(x))[::-1])
        
        # Restore the sign
        result = sign * reversed_x
        
        # Return 0 if the reversed integer overflows the 32-bit limit
        if result < INT_MIN or result > INT_MAX:
            return 0
            
        return result