# ──────────────────────────────────────────────────
# Problem  : 6. Zigzag Conversion
# Difficulty: Medium
# Tags     : String
# Link     : https://leetcode.com/problems/zigzag-conversion/
# Runtime  : 15 ms (beats 42%)
# Memory   : 12556000 (beats 20%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def convert(self, s, numRows):
        # Base case: If 1 row or string is shorter than rows, no zigzag is needed.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings to represent each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        
        # Traverse the string and place characters in the appropriate row
        for char in s:
            rows[cur_row] += char
            
            # Reverse direction when hitting the top or bottom row
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down
            cur_row += 1 if going_down else -1
            
        # Concatenate all rows into a single string
        return ''.join(rows)