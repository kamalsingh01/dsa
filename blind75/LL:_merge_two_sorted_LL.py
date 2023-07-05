# Merging two sorted Linekd List
'''
21. Merge Two Sorted Lists
Easy
18.7K
1.7K
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

URL : https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursive Approach : TC = O(n), SC = O(n) is recursive stack is taken into consideration
        temp_head = ListNode()
        new_head = temp_head
        if list1 is None and list2 is not None:
            return list2
        if list1 is not None and list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        if list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2