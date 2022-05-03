class Solution(object):
    def isOtherChar(self, c):
        ret = True
        if c == '-' or c == '+' or c == ' ':
            ret = False
        if c >= '0' and c <= '9':
            ret = False
        return ret
    def isNumber( self, c):
        ret = False 
        if c >= '0' and c <= '9':
            ret = True
        return ret
    def myAtoi(self, s):
        #-42
        # asdf sd 986 -> 0
        #前面有空格可以但不能有字母#符号标志
        flag = 1
        #是否已经遍历到数字
        flag1 = 0
        flag2 = 0
        #存放符号的数组
        markArr = []
        number = 0
        for i in range(len(s)):
            if flag1 and self.isNumber(s[i]) == False: 
                break
            if (flag1 == 0 and self.isOtherChar(s[i])) or (len(markArr) > 0 and s[i] ==' '):
                return 0
            if s[i] == '-':
                markArr.append(s[i])
                flag = -1 
            if s[i] == '+':
                markArr.append(s[i])
                flag = 1
            if flag1 and self.isNumber(s[i])== False and flag2 == 0:
                return 0
            if s[i] >= '0' and s[i] <= '9':
    #if s[i] =='0' and flag1 == 0:#return 0
               flag1 = 1
               number = number * 10 + int(s[i])
               if i+1 < len(s) and self.isNumber(s[i+1]) == False and s[i+1] != '-' and s[i+1] != '+' and s[i+1] != ' ': 
                    flag2 = 1
        if len(markArr) > 1:
            return 0
        number = number * flag
        if number > 2** 31 - 1:
            number = 2 ** 31 -1
        if number < -(2** 31):
            number = -( 2**31)
        return number                     
s = "42"
print(Solution().myAtoi(s))
