#creating binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root):
    q = []
    m = {}
    level = 0
    count = 0
    q.append(root)
    while(len(q)!=0):
        count = len(q)
        lst = []
        while(count!=0):
            node = q.pop(0)
            print(q)
            lst.append(node.data)
            if node.left!=None:
                q.append(node.left)
            if node.right!=None:
                q.append(node.right)
            count=count-1
            m[level] = lst
        level=level+1
    for l in m.items():
        print(l[1][-0], end=' ')



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.left.right = TreeNode(7)
    root.left.right.left.right.left = TreeNode(8)
    root.left.right.left.right.right = TreeNode(9)

    left_view(root)
