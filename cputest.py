import random
import sys # python 默认递归深度不超过1000，做dfs会比C吃亏
sys.setrecursionlimit(10000000)# 手动修改深度
import time
import datetime
import matplotlib.pyplot as plt
def getTime():
    return datetime.datetime.now()
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    def QuickSort(self, array, i, j):
        if (j - i) < 1:
            return array
        pivot = array[i]
        left = i
        right = j
        flag = 1
        while left < right:
            if flag == 1:
                if array[right] <= pivot:
                    array[left] = array[right]
                    if left + 1 > right:
                        break
                    left = left + 1
                    
                    flag = -flag
                else:
                    if right - 1 < left:
                        break
                    right = right - 1
                    
            if flag == -1:
                if array[left] > pivot:
                    array[right] = array[left]
                    if right - 1 < left:
                        break
                    right = right - 1
                    
                    flag = -flag
                else:
                    if left + 1 > right:
                        break
                    left = left + 1
        #print(left, right)      
        array[left] = pivot
        array = self.QuickSort(array, i ,left - 1)
        array = self.QuickSort(array, left + 1, j)
        return array
nums = []
for i in range(10000):
    nums.append(random.randint(0,1000))
start = getTime()
array = Solution().QuickSort(nums,0,len(nums)-1)
end = getTime()
with open(r'sorted.txt','w') as f:
    f.write(str(array))
f.close()
print('进程耗时: %s' % (end - start))
x=[]
y=[]
x1=[]
y1=[]
for i in range(1,len(array)):
    x1.append(i)
    y1.append(array[i])
    if array[i] < array[i-1]:
        print("------------------------")
plt.plot(x1,y1)
plt.show()
#print(Solution().containsDuplicate(nums))
