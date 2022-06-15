import sys # python 默认递归深度不超过1000，做dfs会比C吃亏
sys.setrecursionlimit(10000000)# 手动修改深度
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        temp1 = list(s)
        temp2 = list(t)
        temp1dict = {}
        for i in range(len(s)):
            if s[i] not in temp1dict.keys():
                temp1dict[s[i]] = 1
            else:
                temp1dict[s[i]] += 1
        #print(temp1dict)
        temp2dict = {}
        for i in range(len(t)):
            if t[i] not in temp2dict.keys():
                temp2dict[t[i]] = 1
            else:
                temp2dict[t[i]] += 1
        #print(temp2dict)
        return temp1dict == temp2dict
        # for i in range(len(temp1)):
        #     for j in range(len(temp2)):
        #         if temp2[j] == temp1[i]:
        #             temp2[j] = temp1[i].upper()
        #             break
        #         if j == len(temp2) - 1:
        #             return False
        # return True
        # temp1 = self.QuickSort(temp1, 0, len(temp1) - 1)
        # temp2 = self.QuickSort(temp2, 0, len(temp2) - 1)
        # #print(temp1,temp2)
        # for i in range(len(temp1)):
        #     if temp1[i] != temp2[i]:
        #         return False
        # return True
#s = "anagram";t = "nagaram"
lines = []
s = ""
with open(r's.txt', 'r') as f:
    lines = f.readlines()
for l in lines:
    s += l.rstrip('\n')
f.close()
lines = []
t = ""
with open(r't.txt', 'r') as f:
    lines = f.readlines()
for l in lines:
    t += l.rstrip('\n')
f.close()
print(Solution().isAnagram(s, t))
