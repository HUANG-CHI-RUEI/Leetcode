# https://www.cnblogs.com/grandyang/p/5285868.html
# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2 31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''
Example:

Given the 2D grid:

INF -1 0 INF
INF INF INF -1
INF -1 INF -1
0 -1 INF INF
After running your function, the 2D grid should be:

3 -1 0 1
2 2 1 -1
1 -1 2 -1
0 -1 3 4
'''
# 1.dfs: 
# TC:O(m*n*4)
# SC:O(m*n*4)
class Solution:
    def walsAndGates(self, room):
        if not rooms:
            return []
        m, n = len(room), len(room[0])
        
        def dfs(x, y, dis):
            if x < 0 or x >= m or y < 0 or y >= n or room[x][y] < dis:
                return 
            room[x][y] = dis
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i+dx, j+dy, dis+1)

        for x in range(m):
            for y in range(n):
                if room[x][y] == '0':
                    dfs(x, y, 0)

# 2. bfs: https://blog.csdn.net/qq_37821701/article/details/104231821
class Solution:
    def walsAndGates(self, room):
         if not rooms:
            return []
        m, n = len(room), len(room[0])

        def bfs(i, j, dis):
            if i < 0 or j < 0 or i >= m or j >= n or room[i][j] < dis:
                return 
            room[i][j] = dis
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                bfs(i+dx, j+dy, dis+1)

        for r in range(m):
            for c in range(n):
                if room[r][c] == '0':
                    bfs(r, c, 0)