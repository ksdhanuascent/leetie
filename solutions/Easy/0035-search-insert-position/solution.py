# ──────────────────────────────────────────────────
# Problem  : 35. Search Insert Position
# Difficulty: Easy
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/search-insert-position/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12852000 (beats 67%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left