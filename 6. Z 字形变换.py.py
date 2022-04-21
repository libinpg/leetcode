class Solution(object):
    def getRow(self, numRows, i):
        row = 0
        col = 0
        if (i + 1) % (2*numRows - 2 ) -1 == -1:
            row = 1
        elif (i + 1) % (2*numRows - 2 ) > numRows -1:
            row = 2*numRows - 1 - (i + 1) % (2*numRows - 2 ) 
        else:
            row=(i + 1) % (2*numRows - 2 ) -1   
                 
        ys = (i + 1) % (2*numRows - 2 ) -1
        qz = int((i+1)/(2*numRows - 2))
        if ys > numRows - 1:
            col = qz*(numRows - 1) + 1 - numRows + ys
        elif ys == -1:
            #ys = numRows
             col = qz*(numRows - 1)-1
        else:
            col = qz*(numRows - 1)  
        return [row,col]
    def initArr(self, row, col):
        ret = []
        for i in range(col):
            temp = []
            for j in range(row):
                temp.append('')
            ret.append(temp)
        return ret
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        arrRow = numRows
        arrCol = self.getRow(arrRow,len(s)-1)[1] +1
        arr = self.initArr(numRows, arrCol)
        i = 0
        for i in range(len(s)):
            row,col = self.getRow(numRows,i)
            arr[col][row] = s[i]
            print(row,col)
        ret = ""
        for i in range(arrRow):
            for j in range(arrCol):
                ret += arr[j][i]
        return ret
               
s = "PAYPALISHIRING"
numRows = 3
#print(Solution().initArr(1, 1))#测试initArr函数
# s="PAYPALISHIRING"
# for i in range(len(s)):
#     print(Solution().getRow(3, i),s[i],i)#测试initArr函数
print(Solution().convert(s, numRows))
