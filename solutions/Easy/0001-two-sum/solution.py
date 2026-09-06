# ──────────────────────────────────────────────────
# Problem  : 1. Two Sum
# Difficulty: Easy
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/two-sum/
# Runtime  : 0 ms (beats 100%)
# Memory   : 13012000 (beats 68%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i