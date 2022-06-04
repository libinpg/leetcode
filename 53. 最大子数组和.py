class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            if nums[i] > 0:
                break
            i += 1
            if i > (len(nums) - 1):
                return max(nums)
        slow = fast = 0
        maxSum = nums[0]#最大和
        flag = 1#slow是否已经移动的标志
        temp = 0
        while True:
            #移动slow到正数的位置
            while nums[slow] < 0 and slow + 1 <= (len(nums) - 1) and fast + 1 <= (len(nums) - 1):
                slow += 1
                fast += 1
            #print(slow,fast)
            if flag:
                temp = nums[slow]
                flag = 0
            if temp > maxSum:
                maxSum = temp
            #移动快指针并计算慢指针到快指针之间的和，如果和小于零,慢指针移动到快指针的位置
            fast += 1
            if fast > len(nums) - 1:
                    break
            temp += nums[fast]
            print("temp=",temp)
            if temp > maxSum:
                maxSum = temp
            if temp < 0:
                slow = fast
                flag = 1
        #print(slow,fast)
        return maxSum
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-2,1]
#nums = [5,4,-1,7,8]
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-2,1]
#nums = [-1,0,-2]
#nums = [-2,-1,-2]
nums = [1,1,-3,-3]
print(Solution().maxSubArray(nums))