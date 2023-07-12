# Implementing STACK data structure using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            self.head.next = None
            self.size+=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size+=1

    def pop(self):
        if self.head==None:
            print("Underflow")
            return
        else:
            temp = self.head.data
            self.head = self.head.next
            self.size -=1
            print("Popped: ",temp)
            return

        
    def get_size(self):
        return self.size
    
    def isEmpty(self):
        if self.size:
            return False
        return True
    
    def top(self):
        if self.head:
            return self.head.data
        else:
            return "Stack Empty"
    
    def print_stack(self):
        temp = self.head
        while(temp):
            print( temp.data, end="")
            temp = temp.next
            if temp is None:
                break
            print("->",end="")
        print()

    
if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(9)
    s.push(2)
    s.print_stack()
    print("Top: ", s.top())
    print("Size: ",s.get_size())
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
    print("Size: ",s.get_size())
    print("Top: ", s.top())
    s.pop()
    s.pop()
    print("Size: ",s.get_size())
    print("Top: ", s.top())
