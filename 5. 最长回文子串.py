class Solution(object):
    def isHw(self, pSlow, pFast, s):
        #print(pSlow, pFast, s)
        ret = 1
        while pSlow < pFast:
            if s[pSlow] != s[pFast]:
                ret = 0
                return ret
            pSlow += 1
            pFast -= 1
        return ret
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLong = 0
        maxLongStr = ""
        pSlow = 0
        pFast = pSlow + maxLong
        while pSlow <= (len(s) - 1):
            if self.isHw(pSlow, pFast, s):
                if (pFast - pSlow + 1) > maxLong:
                    maxLong = pFast - pSlow + 1
                    maxLongStr = s[pSlow:pFast + 1]
            if pFast == len(s) - 1:
                pFast = pSlow + maxLong
                pSlow += 1
            pFast += 1
            if pFast > (len(s) - 1):
                break
        return maxLongStr
s = "cbbd"
#print(Solution().isHw(2, 2, s))#测试isHw函数
print(Solution().longestPalindrome(s))
'''
执行用时：
9324 ms
, 在所有 Python 提交中击败了
5.02%
的用户
内存消耗：
13.1 MB
, 在所有 Python 提交中击败了
69.57%
的用户
'''
