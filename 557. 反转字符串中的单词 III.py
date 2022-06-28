from audioop import reverse


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        #print(words)
        ret = ""
        for w in words:
            ret += w
            ret += " "
        ret = ret.rstrip(" ")
        return ret
        #print(ret)
s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
