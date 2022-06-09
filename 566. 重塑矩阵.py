class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        #构造矩阵
        matrix = []
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(0)
            matrix.append(temp)
        #print(matrix)
        #获取矩阵长度
        matrixLength = len(mat)*len(mat[0])
        #print(matrixLength)
        #将mat展开为一维数组
        array = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                array.append(mat[i][j])
        #print(array)
        if not len(array) == r*c:
            return mat
        k = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = array[k]
                k += 1
        #print(matrix)
        return matrix
mat = [[1,2],[3,4]]
r = 1
c = 4
print(Solution().matrixReshape(mat, r, c))
