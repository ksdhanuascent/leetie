# ──────────────────────────────────────────────────
# Problem  : 239. Sliding Window Maximum
# Difficulty: Hard
# Tags     : Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue, Range Minimum/Maximum Query
# Link     : https://leetcode.com/problems/sliding-window-maximum/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12476000 (beats 0%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque() 
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res