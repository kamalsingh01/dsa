# 1290. Convert Binary Number in a Linked List to Integer

'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

 

Example 1:
            1->0->1

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        count=0
        while head!=None:
            count+=1
            head = head.next
        return count

    def getDecimalValue(self, head: ListNode) -> int:
        #using iterative method
        
        # temp = head
        # result = 0
        # n = 1
        # while(temp.next!=None):
        #     temp = temp.next
        #     n+=1
        # temp = head
        # while(temp!=None):
        #     result = result+(temp.val*(2**(n-1)))
        #     n-=1
        #     temp = temp.next
        # return result

        #using recursion
        if head == None:
            return 0
        len = self.length(head)
        ans = head.val*(2**len)
        return ans+getDecimalValue(head.next)
        
