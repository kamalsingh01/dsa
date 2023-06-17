# reverse a linked list
'''
206. Reverse Linked List
Easy
18.2K
338
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

URL : https://leetcode.com/problems/reverse-linked-list/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative method
        if head is None:
            return head
        prev, current = head, head
        nest = head.next
        head.next = None
        while nest is not None:
            current = nest
            nest = nest.next
            current.next = prev
            prev = current
        return current

        #recursive method
        