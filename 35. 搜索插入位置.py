class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = len(nums)
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                ret = i
                break
        return ret
nums = [1,3,5,6];target = 5
nums = [1,3,5,6];target = 7
print(Solution().searchInsert(nums, target))