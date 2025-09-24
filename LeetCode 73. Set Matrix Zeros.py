class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = []
        col = []

        for i, n in enumerate(matrix):
            for l, m in enumerate(matrix[i]):
                if matrix[i][l] == 0:
                    row.append(i)
                    col.append(l)

        for r, val in enumerate(matrix):
            if r in row:
                matrix[r] = [0 for i in range(len(matrix[0]))]
                continue
            for c, num in enumerate(matrix[r]):
                if c in col:
                    matrix[r][c] = 0
