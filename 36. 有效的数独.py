from operator import truediv

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #print(board)
        ret = True
        #判断行是否满足规则
        for i in range(len(board)):
            temp = []
            for j in range(len(board[i])):
                if board[i][j] in temp and board[i][j] != '.':
                    ret = False
                    return ret
                temp.append(board[i][j])
        #判断列是否满足规则
        for i in range(len(board)):
            temp = []
            for j in range(len(board[i])):
                if board[j][i] in temp and board[j][i] != '.':
                    ret = False
                    return ret
                temp.append(board[j][i])
        #判断宫格内是否满足规则
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                #print(i,j)
                temp = []
                for l in range(0, 3):
                     for m in range(0, 3):
                        #print(l + i,m + j)
                        if board[l + i][m + j] in temp and board[l + i][m + j] != '.':
                             ret = False
                             return ret
                        temp.append(board[l + i][m + j]) 
        return True
                        #     return ret
                        # temp.append(board[j][i])
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
board = [[".",".",".",".","5",".",".","1","."]
         ,[".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
print(Solution().isValidSudoku(board))
