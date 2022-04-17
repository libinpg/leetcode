class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and not (i == j):
                    ret.append(i)
                    ret.append(j)
                    return ret
        return ret
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))
'''
执行用时：
3720 ms
, 在所有 Python 提交中击败了
6.78%
的用户
内存消耗：
13.9 MB
, 在所有 Python 提交中击败了
33.58%
的用户
'''
        
