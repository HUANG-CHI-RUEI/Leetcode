# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]

# https://blog.csdn.net/danspace1/article/details/86654851
# https://www.youtube.com/watch?v=y9DosONDeYk&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque()
        queue.append([root, 0])
        lookup = defaultdict(list)
        res = []

        while queue:
            for _ in range(len(queue)):
                node, column = queue.popleft()
                lookup[column].append(root.val)

                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))
        left = min(lookup.keys())
        right max(lookup.keys())

        for i in range(left, right + 1):
            res.append(lookup[i])
        return res   


