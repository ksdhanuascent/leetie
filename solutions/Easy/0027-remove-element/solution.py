# ──────────────────────────────────────────────────
# Problem  : 27. Remove Element
# Difficulty: Easy
# Tags     : Array, Two Pointers
# Link     : https://leetcode.com/problems/remove-element/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12428000 (beats 18%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # This will track the position for the next valid element
        
        for i in range(len(nums)):
            # If the current element is not the value we want to remove
            if nums[i] != val:
                # Move it to the 'k' index and increment 'k'
                nums[k] = nums[i]
                k += 1
                
        # k represents the number of elements not equal to val
        return k