# Remove linked List elements from the given value of the node
'''
203. Remove Linked List Elements
Easy

Companies
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

URL : https://leetcode.com/problems/remove-linked-list-elements/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC = O(n), SC = O(1)
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        prev = head
        while temp:
            if temp.val==val:
                if temp is head:
                    head = head.next
                    temp = head 
                    prev = head
                    continue
                else:
                    temp = temp.next
                    prev.next = temp
                    continue    
            prev = temp
            temp = temp.next
        return head