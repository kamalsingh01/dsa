# creating a general tree in python.
'''
    > In general, Tree(General Tree) can have any number of child and can span upto any number of levels, but for binary tree only two childs are allowed.
    > Tree supports hierarchical data and is applicable to data like Organisational Data, Family Tree, Directory System
    > Tree is a recursive data structure, where any child node can also become parent.
    > First node will be the root node.
'''


# Tree node  - Every node in a tree belongs to this user-defined class
class TreeNode:
    def __init__(self, data):
        self.data = data  # value in the node
        self.children = []  # list for multiple child
        self.parent = None  # for root node, parent is none, but needs to be updated for every child node

    def add_child(self, child):
        child.parent = self
        # self contains node instance for which child is created and child is already a TreeNode instance passed in this method
        self.children.append(child)  # child name is added to child list for parent node

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__"if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level


def make_tree():
    root = TreeNode("Electronics")

    # creating child nodes,
    laptop = TreeNode("Laptop")
    cellphones = TreeNode("Cellphones")
    television = TreeNode("television")

    # adding children
    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(television)

    #adding children of each child node of root

    laptop.add_child( TreeNode("Mac"))
    laptop.add_child( TreeNode("Dell"))
    laptop.add_child( TreeNode("HP"))

    cellphones.add_child( TreeNode("iphone"))
    cellphones.add_child( TreeNode("vivo"))
    cellphones.add_child( TreeNode("samsung"))

    television.add_child( TreeNode("sony"))
    television.add_child( TreeNode("LG"))

    return root

if __name__ == "__main__":
    root = make_tree()
    root.print_tree()
    pass
