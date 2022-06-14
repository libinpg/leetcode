class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        遍历ransomNote, 每个字符在magazine中第一次出现的位置变为大写字母
        如果搜索不到字符, 返回false, ransomNote遍历到最后一个字符, 返回true 
        '''
        for i in range(len(ransomNote)):
            for j in range(len(magazine)):
                if magazine[j] >= 'a' and magazine[j] <= 'z' and magazine[j] == ransomNote[i]:
                    temp = list(magazine)
                    #print(temp)
                    temp[j] = temp[j].upper()
                    magazine = ''.join(i for i in temp)
                    #print(magazine)
                    break
                if j == (len(magazine) - 1):
                    return False
        return True                 
ransomNote = "aa";magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
