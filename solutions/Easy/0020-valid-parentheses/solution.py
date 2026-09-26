# ──────────────────────────────────────────────────
# Problem  : 20. Valid Parentheses
# Difficulty: Easy
# Tags     : String, Stack, Bracket Sequences
# Link     : https://leetcode.com/problems/valid-parentheses/
# Runtime  : 7 ms (beats 13%)
# Memory   : 12368000 (beats 97%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isValid(self, s):
        stack=[]
        for c in s:
            if c in "{[(":
                stack.append(c)
            elif len(stack) == 0 or (c == "}" and stack[-1] != '{') or (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()
        return len(stack)==0