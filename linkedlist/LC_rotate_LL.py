# Rotate the linked List by given K number of nodes.
'''
61. Rotate List
Medium
8
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

URL : https://leetcode.com/problems/rotate-list/description/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        last= head
        n=0
        while(last.next!= None):
           n+=1
           last = last.next
        n=n+1
        temp = head
        prev = head
        k = k % n
        if k==0:
            return head
        cutoff = n-k
        while((cutoff) > 0):
            cutoff-=1
            prev = temp
            temp = temp.next
        prev.next = None
        last.next = head
        head = temp
        return head
