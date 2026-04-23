# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""
Time = O(n)
Space = O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return head
            rtn = head
            low = head
            high = head.next
            last = head
            while last.next != None:
                 last = last.next
            while high and low:
                if low.val == high.val:
                    high = high.next
                else:
                    low.next = high
                    low = low.next
                    high = high.next
            if low.val == last.val:
                low.next = None
            return rtn

