# ──────────────────────────────────────────────────
# Problem  : 8. String to Integer (atoi)
# Difficulty: Medium
# Tags     : String
# Link     : https://leetcode.com/problems/string-to-integer-atoi/
# Runtime  : 4 ms (beats 45%)
# Memory   : 12408000 (beats 23%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def myAtoi(self, s):
        # 1. Ignore leading whitespace
        s = s.lstrip()
        
        # Return 0 if string is empty after stripping
        if not s:
            return 0
            
        sign = 1
        i = 0
        
        # 2. Determine signedness
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        res = 0
        
        # 3. Convert characters to integer
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply the sign
        res *= sign
        
        # 4. Rounding (Clamp to 32-bit signed integer range)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res