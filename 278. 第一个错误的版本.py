class Solution(object):
    def isBadVersion(self, version):
        return None
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p1 = 1
        p2 = n
        while p1 != p2:
            p = int((p1 + p2)/2)
            if self.isBadVersion(p) == False:
                p1 = p + 1
            elif self.isBadVersion(p) == True:
                p2 = p
            else:
                return p
            if p1 == p2:
                if self.isBadVersion(p1) == True:
                    return p1
                else:
                    break
        return 1
n = 5;bad = 4
print(Solution().firstBadVersion(n))
