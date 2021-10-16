# 311. Sparse Matrix Multiplication 稀疏矩陣相乘

# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
#  1. https://blog.csdn.net/qq_37821701/article/details/108821029
# TC:O(n^3)
# SC:O(n^2)

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])

        nB = len(B[0])
        
        ans = [[0] * nB for _ in range(m)]

        for i in range(m):
            for j in rnage(n):
                for b_j in range(nB):
                    ans[i][b_j] += A[i][j] * B[j][b_j]
        
        return ans


# 2. Optimized, T: O(n^2)
# Time:  O(m * n)
# Space: O(m * n)


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def encode(matrix):
            dense_matrix = {}
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]:
                        dense_matrix[(i, j)] = matrix[i][j]
            return dense_matrix

        def decode(dense_matrix, row, col):
            sparse_matrix = [[0] * col for _ in range(row)]
            for (i, j), val in dense_matrix.items():
                sparse_matrix[i][j] = val

            return sparse_matrix

        A_dense = encode(A)
        B_dense = encode(B)
        ans_dense = defaultdist(int)
        
        for (i, j) in A_dense.keys():
            for k in range(len(B[0])):
                if (j, k) in B_dense:
                    ans_dense[(i, k)] += A_dense[(i, j)] * B_dense[(j, k)]

        return decode(ans_dense, len(A), len(B[0]))

