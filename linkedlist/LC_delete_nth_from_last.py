# Delete nth node fromlast of linked list given the value of n
'''
19. Remove Nth Node From End of List

Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?



'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        node = head
        current = head
        prev = None
        i=1
        # solution in two passes
        while(i<n):
            node = node.next
            i+=1
        while(node.next is not None):
            node = node.next
            prev = current
            current = current.next

        # solution in one pass:-

        # while(node.next is not None):
        #     if i<n:
        #         node = node.next
        #     if i==n:
        #         current, prev = head, head
        #     if i>n:
        #         node = node.next
        #         prev = current
        #         current = current.next
        #     i+=1

        if current==head:
            head = head.next
        if prev is not None:
            prev.next = current.next

        return head
