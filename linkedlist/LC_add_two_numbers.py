# Add two numbers given in the form of linked List
'''
2. Add Two Numbers
Medium

Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach
        carry = 0
        lst = []
        while(l1 is not None or l2 is not None):
            if l1 is None:
                sumx = l2.val + carry
            elif l2 is None:
                sumx = l1.val + carry
            elif l1 and l2:
                sumx = l1.val + l2.val + carry
            carry = sumx//10
            sumx = sumx%10
            lst.append(sumx)
            # if head is None:
            #     head.val = sumx
            #     head.next = node
            #     node.val = carry
            # else:
            #     node.val = sumx
            #     node1 = ListNode()
            #     node1 = node.next
            #     node = node1
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry>0:
            # node.val = carry
            # node1 = ListNode(None, None)
            # node1 = node.next
            # node = node1
            lst.append(carry)
        head = ListNode()
        #node = ListNode()
        node = head
        i=0
        while(i<len(lst)):
            node1 = ListNode()
            node.val = lst[i]
            node.next = node1
            prev = node
            node = node.next
            i+=1
        prev.next = None
        print(lst)
        return head