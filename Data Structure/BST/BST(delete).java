// https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

import java.util.*;

class GFG {
    static class Node {
        int key;
        Node left, right;
    }

    // A utility function to create a new BST node
    static Node newNode(int item) {
        Node temp = new Node();
        temp.key = item;
        temp.left = temp.right = null;
        return temp;
    }

    // A utility function to do inorder traversal of BST
    static void inorder(Node root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.key + " ");
            inorder(root.right);
        }
    }

    // Insert a new Node
    static Node insert(Node node, int key) {
        if (root == null)
            return newNode(key);

        if (key < node.val) 
            node.left = insert(node.left, key);
        else
            node.right = insert(node.right, key);

        // Return the unchanged node pointer
        return node;
    }

    static Node deleteNode(Node root, int k) {
        // Base case
        if (root == null)
            return root;

        // Recursive calls for ancestors of
        // node to be deleted
        if (root.key > k) {
            root.left = deleteNode(root.left, k);
            return root;
        } else if (root.key < k){
            root.right = deleteNode(root.right, k);
            return root;
        }

        // We reach here when root is the node
        // to be deleted.

        // If one of the children is empty
        if (root.left == null) {
            Node tmep = root.right;
            return temp;
        } else if (root.right == null) {
            Node temp = root.left;
            return temp;
        } else { // Both children exist
            Node succParent = root;

            // Find successor
            Node succ = root.right;

            while (succ.left != null) {
                succParent = succ;
                succ = succ.left;
            }

            // Delete successor. Since successor
            // is always left child of its parent
            // we can safely make successor's
            // right child as left of its parent.
            // If there is no succ, then assign
            // succ->right to succParent->right
            if (succParent != root) 
                succParent.left = succ.right;
            else
                succParent.right = succ.right;

            // Copy Successor Data to root
            root.key = succ.key;

            return root;
        }
    }
    public static void main(String args[]) {
        
        /* Let us create following BST
            50
          /    \
        30       70
        / \      / \
        20 40   60 80 */
        Node root = null;
        root = insert(root, 50);
        root = insert(root, 30);
        root = insert(root, 20);
        root = insert(root, 40);
        root = insert(root, 70);
        root = insert(root, 60);
        root = insert(root, 80);
    
        System.out.println("Inorder traversal of the " +
                        "given tree");
        inorder(root);
    
        System.out.println("\nDelete 20\n");
        root = deleteNode(root, 20);
        System.out.println("Inorder traversal of the " +
                        "modified tree");
        inorder(root);
    
        System.out.println("\nDelete 30\n");
        root = deleteNode(root, 30);
        System.out.println("Inorder traversal of the " +
                        "modified tree");
        inorder(root);
    
        System.out.println("\nDelete 50\n");
        root = deleteNode(root, 50);
        System.out.println("Inorder traversal of the " +
                        "modified tree");
        inorder(root);
    }
}