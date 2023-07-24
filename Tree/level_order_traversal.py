from collections import deque

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def MakeTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.data, end=' ')
    print_tree(root.right)

def level_order(root):
    q = deque()
    q.append(root)
    ans = []
    while(len(q)!=0):
        size = len(q)
        lst = []
        for i in range(size):
            temp = q.popleft()
            if temp.left is not None:
                q.append( temp.left)
            if temp.right is not None:
                q.append( temp.right)
            lst.append(temp.data)
        ans.append(lst)
    return ans

if __name__ == "__main__":
    root = MakeTree()
    print("In-order: ",end='')
    print_tree(root)
    ans = level_order(root)
    print("Level-order: ",ans)