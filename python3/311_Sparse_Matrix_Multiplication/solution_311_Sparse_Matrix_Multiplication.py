class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # m1 * n1 x m2 * n2 = m1 * n2
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        m1, n1, n2 = len(mat1),len(mat1[0]), len(mat2[0])
        for i in range(m1):
            for j in range(n1):
                if mat1[i][j]:
                    for k in range(n2):
                        result[i][k] += mat1[i][j] * mat2[j][k]
        return result
