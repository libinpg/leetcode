class Solution(object):
    stack = []
    front = -1
    rear = -1
    def addNum2Stack(self, num):
        self.stack.append(num)
        self.front = self.front + 1
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ret = True
        tempx = x
        if tempx < 0:
            return False
        if x >= 0 and x <= 9:
            return True
        tempx = x
        while tempx != 0:
            self.addNum2Stack(tempx % 10)
            tempx = int(tempx / 10)
        while x != 0:
            if x % 10 != self.stack[self.front]:
                ret = False
            self.front = self.front - 1
            x = int(x / 10)
        return ret
x = 11
print(Solution().isPalindrome(x))
