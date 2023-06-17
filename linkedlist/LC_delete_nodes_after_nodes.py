# 	1474 Delete N Nodes After M Nodes of a Linked List

'''
URL : https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
'''

#creating node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while True:
                if current.next is None:
                    break
                current = current.next
            current.next = newnode

    def print_list(self,head):
        if self.head == None:
            print("Empty Linked List")
            return
        current = self.head
        while True:
            print(current.data, end="->")
            if current.next is None:
                break
            current = current.next
        

def delete_nodes_after_nodes( head ):
    n = int(input("\nEnter no. of ndoes to delete): "))
    m = int(input("\nEnter node place after which to delete): "))
    current = head
    while(m>1):
        m-=1
        current = current.next
    temp = current
    while(n>=0):
        if current is None:
            print("Index out of range")
            break
        current = current.next
        n-=1
    temp.next = current
    return head

if __name__ == "__main__":
    x = int(input("Enter the size of list:"))
    print("Enter Linkedlist Elements: ")
    num = int(input())
    ll = LinkedList()
    head = Node(num)
    ll.add_node(head)
    for i in range(x-1):
        num = int(input())
        node = Node(num)
        ll.add_node(node)
    ll.print_list(head)
    delete_nodes_after_nodes(ll.head)
    print("Updated List: ", end = '')
    ll.print_list(head)