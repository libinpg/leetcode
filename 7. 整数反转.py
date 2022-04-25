import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        #判断x正负
        if x < 0:
           flag = -1
           x = -x
        elif x == 0:
            return 0 
        #构造一个栈
        stack = []
        front = rear = -1
        #将x的每个数字压入栈中
        while x != 0:
            stack.append(x % 10)
            x = int(x / 10)
            rear += 1
        ret = 0
        #出栈元素
        while rear != front:
            front += 1
            ret = ret * 10 + stack[front]
        ret = flag * ret
        if ret > 2 ** 31 - 1 or ret < -(2 ** 31):
            ret = 0
        return ret
x = -123
print(Solution().reverse(x))
