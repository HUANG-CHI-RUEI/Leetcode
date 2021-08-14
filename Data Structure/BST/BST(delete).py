# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def insert(node, val):
    
    if node is None:
        return Node(val)

    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)

    return node 

def deleteNode(root, val);

    # Base case
    if root is None:
        return root

    if val < root.val:
        root.left = deleteNode(root.left, val)
        return root 
    elif val > root.val:
        root.right = deleteNode(root.right, val)
        return val

    # If one of the children is empty
    if root.left is None:
        temp = root.right
        return temp
    elif root.right is None:
        temp = root.left
        return temp
    
    succParent = root
    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left 

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
    
    root.val = succ.val

    return root

# Driver code
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """
       
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print("Inorder traversal of the given tree")
inorder(root)
 
print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)