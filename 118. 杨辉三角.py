class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(0)
            ret.append(temp)
        #print(ret)
        for i in range(len(ret)):
            ret[i][0] = 1
            ret[i][-1] = 1
        #print(ret)
        for i in range(1, len(ret) - 1):
            p1 = 0
            p2 = 1
            p3 = 1
            while p2 <= len(ret[i]) - 1:
                ret[i + 1][p3] = ret[i][p1] + ret[i][p2]
                p1 += 1
                p2 += 1
                p3 += 1
        #print(ret)
        return ret
numRows = 5
print(Solution().generate(numRows))