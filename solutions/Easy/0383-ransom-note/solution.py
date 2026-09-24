# ──────────────────────────────────────────────────
# Problem  : 383. Ransom Note
# Difficulty: Easy
# Tags     : Hash Table, String, Counting
# Link     : https://leetcode.com/problems/ransom-note/
# Runtime  : 55 ms (beats 20%)
# Memory   : 12584000 (beats 88%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False