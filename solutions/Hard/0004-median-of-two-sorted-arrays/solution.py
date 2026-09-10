# ──────────────────────────────────────────────────
# Problem  : 4. Median of Two Sorted Arrays
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer
# Link     : https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12608000 (beats 15%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Always run binary search on the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition the smaller array
            partition1 = (low + high) // 2
            # Partition the larger array to keep left and right halves balanced
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases using infinity if the partition is at the extreme ends
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if the partition is valid
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is odd, the median is the max of the left elements
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # If total length is even, it's the average of max left and min right
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            
            # If maxLeft1 is too large, move the search space to the left
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            # Otherwise, move the search space to the right
            else:
                low = partition1 + 1