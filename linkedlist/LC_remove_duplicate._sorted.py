# Remove duplicate node from a sorted linked list
'''
3. Remove Duplicates from Sorted List
Easy

Companies
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Accepted
1.2M
Submissions
2.4M
Acceptance Rate
50.9%

URL : https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        #Optimal Approach
        temp = head
        while(temp and temp.next):
            if temp.val == temp.next.val:
                temp.next = temp.next.next
                continue
            temp = temp.next


        #Brute Force approach
        temp, dup = head, head.next
        while( dup is not None ):
            while(temp.val == dup.val):
                temp.next = dup.next
                dup = dup.next
                if dup is None:
                    break
            temp = dup
            if dup is not None and dup.next is not None:
                dup = dup.next
        return head
