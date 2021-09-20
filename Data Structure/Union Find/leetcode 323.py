# Number of Connected Components in an Undirected Graph
# https://www.youtube.com/watch?v=gKKATlgNNqM
# https://www.youtube.com/watch?v=8f1XPm4WOUc
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
#  write a function to find the number of connected components in an undirected graph.

'''
1. UnionFind:
TC:O(e):e is the number of edges or the length of the edges array
SC:O(n), is the number of nodes
'''
 class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        # parent = list(range(n))
        rank = [1] * n

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = find(parent[res])
                res = parent[res]
            return res

        def union(x, y):
            p1, p2 = find(x), find(y)

            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

#############################################
'''
2. DFS:
TC:O(m+n), m is number of edges, n is second loop
SC:O(2n) = n, graph take n space, and dfs take n, too.
'''
 class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        visited = set()
        ans = 0

        graph = defaultdict(list)

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            graph[node1].append(node2)
            graph[node2].append(node1)

        for i in range(n):
            if i not in visited:
                ans += 1
                visited.add(i)
                dfs(i)

        return ans