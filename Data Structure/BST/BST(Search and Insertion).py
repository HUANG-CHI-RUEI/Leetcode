# Inorder traversal of BST always produces sorted output.
# We can construct a BST with only Preorder or Postorder or Level Order 
# traversal. 
# Note that we can always get inorder traversal by sorting the only given traversal.

class Node: 
    def __init__(self, key):
        self.left = None
        self.right = Node
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val > key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

def search(root, key):

    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.left, key)
    return search(root.right, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)



