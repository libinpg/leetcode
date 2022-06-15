class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        找到最后一个为零的位置, 从这里开始向前遍历数组, 当遍历字符为0时,开始从
        当前位置向最后依次进行交换, 直至将0交换到末尾位置。
        """
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                flag = i
        #print(flag)
        count = 0
        for i in range(flag, -1, -1):
            if nums[i] == 0:
                #print("------------------")
                for j in range(i,len(nums) - 1):
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                #print(nums)
            count += 1
        return nums
#nums = [0,1,0,3,12]
#nums = [1,0,0]
nums = [0,0,1]
print(Solution().moveZeroes(nums))
