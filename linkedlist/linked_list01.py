# Node and Linked List Creation

#creating node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating linkedllist
class LinkedList:
    def __init__(self):
        self.head = None    #initially, linked list is empty, so head points to null

    def insert(self, newnode):
        # head->newnode->None
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while True:
                if current.next == None:
                    break
                current = current.next
            current.next = newnode

    def printlist(self,head):
        if self.head == None:
            print("Empty Linked List")
            return
        current = self.head
        while True:
            # if current == None:
            #     break
            print(current.data, end="->")
            if current.next == None:
                break
            current = current.next

    
if __name__ == "__main__":
    head = Node("John")
    linkedlist = LinkedList() # new linkedlist
    # linkedlist.insert(head)
    # secondNode = Node("Ben")
    # linkedlist.insert(secondNode)
    # thirdNode = Node("Mathew")
    # linkedlist.insert(thirdNode)
    linkedlist.printlist(head)
