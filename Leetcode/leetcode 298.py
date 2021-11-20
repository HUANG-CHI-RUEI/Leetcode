# Given a binary tree, find the length of the longest consecutive sequence path.html

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#1.  http://hk.noobyard.com/article/p-yyoramkg-gs.html
# TC:O(n)
# SC:O(h)
class Solution(object):
    def longestConsecutive(self, root):
        self.max_len = 0

        def  helper(root):
            if not root:
                return 0
            left_len = helper(root.left)
            right_len = helper(root.right)

            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1)
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len)

            return cur_len

        helper(root)
        return self.max_len
                

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/298.%20Binary%20Tree%20Longest%20Consecutive%20Sequence.md
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, curLen):
            self.result = max(curLen, self.result)
            if root.left:
                if root.left.val == root.val + 1:
                    dfs(root.left, curLen + 1)
                else:
                    dfs(root.left, 1)
            if root.right:
                if root.right.val == root.val + 1:
                    dfs(root.right, curLen + 1)
                else:
                    dfs(root.right,1)
                    
        if not root: return 0

        self.result = 0
        dfs(root, 1)
        return self.result
