# ──────────────────────────────────────────────────
# Problem  : 11. Container With Most Water
# Difficulty: Medium
# Tags     : Array, Two Pointers, Greedy
# Link     : https://leetcode.com/problems/container-with-most-water/
# Runtime  : 108 ms (beats 78%)
# Memory   : 20844000 (beats 26%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # The height of the container is limited by the shorter line
            current_height = min(height[left], height[right])
            # The width of the container is the distance between the lines
            current_width = right - left
            
            # Calculate the current area and update the maximum if necessary
            current_area = current_height * current_width
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water