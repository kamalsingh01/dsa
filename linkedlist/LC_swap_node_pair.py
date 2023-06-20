# swap adjacent node pair in a linked list
'''
24. Swap Nodes in Pairs
Medium

Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100 

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            temp = head
        temp_value = 0
        while( temp is not None and temp.next is not None ):
            temp_value = temp.val
            temp.val= temp.next.val
            temp.next.val = temp_value
            temp = temp.next.next
            
        return head