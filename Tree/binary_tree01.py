'''
    > Binary Tree in which each node can only have at most 2 child nodes( left child & right child ) and 1 parent node.
    > If the tree is empty, value of root is NULL.
    > all the elements are unique in binary search Tree
    > Traversals in Python: 
        :: Traversal can be done in two ways: Iterative and Recursive

        1. Breadth First Search (ITERATIVE)
        2. Depth First Search( RECURSIVE) - In-order Traversal, Pre-order Traversal, Post-Order Traversal

    > IN-ORDER Traversal  - Left-Root-Right
    > PRE-ORDER Traversal - Root-Left-Right
    > POST-ORDER Traversal - Left-Right-Root
    
    > Preferably, we always reach left subtree then we go to right sub-tree

   

'''
#creating a binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printinorder(root):

    if root:
        printinorder(root.left)
        print(root.val, end = ' ')
        printinorder(root.right)

def printpreorder(root):

    if root:
        print(root.val, end = ' ')
        printpreorder(root.left)
        printpreorder(root.right)

def printpostorder(root):

    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val, end = ' ')

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(10) 

    # Three BFS traversals
    print("In-order Traversal Output: ")
    printinorder(root)    
    print("\nPre-order Traversal Output: ")
    printpreorder(root)   
    print("\nPost-order Traversal Output: ")
    printpostorder(root)


# Time Complexity : O(N), where N is number of nodes in tree, SC = Auxiliary space of O(N), height of the tree