# ──────────────────────────────────────────────────
# Problem  : 21. Merge Two Sorted Lists
# Difficulty: Easy
# Tags     : Linked List, Recursion
# Link     : https://leetcode.com/problems/merge-two-sorted-lists/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12376000 (beats 84%)
# Language : python
# Copyright: (c) 2026 ksdhanuascent. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists as long as neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer forward
            current = current.next
            
        # If any elements remain in either list, attach them to the end
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # Return the merged list, skipping the dummy node
        return dummy.next