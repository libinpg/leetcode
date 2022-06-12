class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        #print(rows,cols)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return matrix
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))
