# Check whether a linked List is Palindrome or not
'''
234. Palindrome Linked List
Easy

Companies
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 
Input: head = [1,0,1]
Output: True

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC = O(n), SC = O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        fast, slow = head, head
        mid = head
        temp1 = head
        while fast and fast.next:
            fast = fast.next.next
            mid = slow
            slow = slow.next
        prev_new = slow
        slow = slow.next
        prev_new.next = None
        while(slow):
            current = slow
            slow = slow.next
            current.next = prev_new
            prev_new = current
        mid.next = prev_new
        temp2 = prev_new
        while(temp1!=mid.next):   # while(temp2): ??
            if temp1.val!= temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True