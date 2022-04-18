class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #定义两个子串指针, p1慢指针,p2快指针
        p1 = p2 = 0
        #如果子串为空,返回零
        if s == "":
            return 0
        if s == " ":
            return 1
        #如果子串为单字符,返回1
        if len(s) == 1:
            return 1
        #存放子串的数组,其中的元素应该是互不重复
        temp = []
        #最长子串的长度
        ret = -1
        flag = 0
        while p2 < len(s):
            #如果快指针指向的字符串在子串数组中已经存在,慢指针应该跳到重复字符的位置
            if s[p2] in temp:
               while s[p1] != s[p2]:
                        p1 += 1
                        #print("p1指针移动", "p2=" + str(p2), "p1=" + str(p1))
               p1 += 1
            temp = list(s)[p1:p2+1]
            #if p2 == len(s) - 1 and flag == 0:
            #    return len(s)
            #如果子串的长度大于最大长度,即已经找到了大于最大长度的字符串
            if len(temp) > ret:
                ret = len(temp)
                #print(temp, p1, p2)
            p2 +=1
            #print("p2=" + str(p2), "p1=" + str(p1))
        return ret
s = "aabaab!bb"
print(Solution().lengthOfLongestSubstring(s))
'''
执行用时：
6716 ms
, 在所有 Python 提交中击败了
5.01%
的用户
内存消耗：
13.5 MB
, 在所有 Python 提交中击败了
63.53%
的用户
'''
