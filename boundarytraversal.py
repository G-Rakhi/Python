class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def print_left_boundary(root):
    if root:
        if root.left:
            print(root.value,end=' ')
            print_left_boundary(root.left)
        if root.right:
            print_left_boundary(root.right)

def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left==None and root.right==None:
            print(root.value,end=' ')
        print_leaves(root.right)

def print_right_boundary(root):
    if root:
        if root.right:
            print_right_boundary(root.right)
            print(root.value,end=' ')
        if root.left:
            print_right_boundary(root.left)
           

def boundary_leaves(root):
    if root:
        print(root.value,end=' ')
        print_left_boundary(root.left)
        print_leaves(root.left)
        print_leaves(root.right)
        print_right_boundary(root.right)

#driver code
root=Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left=Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
root.right.right=Node('G')

boundary_leaves(root)
