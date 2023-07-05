# Re order a linked list

'''
143. Reorder List
Medium
9.1K
301
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

URL : https://leetcode.com/problems/reorder-list/description/


'''

# TC = O(n)+O(n/2), SC = O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        fast = head
        current = slow.next
        mid, prev = slow, slow
        while(current):
            slow = current
            current = current.next
            slow.next = prev
            prev = slow
        current = fast.next
        mid.next = None
        while(slow.next):
            fast.next = slow
            slow = slow.next
            prev.next = current
            fast = current
            current = current.next
            prev = slow
        del slow
        del fast
        del current
        del prev