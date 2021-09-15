# 305: number of Island II
# https://www.youtube.com/watch?v=L3Ml5A_0szU

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]])  -> List[int] :
        uf = UnionFind(m * n)
        visit = set()
        res, island = [], 0
        for r, c in positions:
            p = r * n + c
            if p not in visit: # prevent same positions
                visit.add(p)
                island += 1

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < m and 0 <= nc <= n:
                    np = nr * n + nc
                    if np in visit and uf.find(p) != uf.find(np):
                        uf.union(p, np)
                        island -= 1
            res.append(island)
        return res

# https://blog.csdn.net/qq_37821701/article/details/108414572
class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.count = 0

    def find(self, p):
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def add_island(self, pos):
        if pos not in self.parent:
            self.parent[pos] = pos
            self.count += 1

    def union(self, p, q):
        rootp, rootq = self.find(p), self.find(q)
        if rootp != rootq:
            self.parent[rootp] = self.parent[rootq]
            self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]])  -> List[int] :
        uf = UnionFind()
        ans = []
        for (r, c) in positions:
            uf.add_island((r, c))
            for neigh in  [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if neigh in uf.parent:
                    uf.union((r, c), neigh)
            ans.append(uf.count)

        return ans