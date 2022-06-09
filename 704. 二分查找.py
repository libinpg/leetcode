class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        p1 = 0
        p2 = len(nums) - 1
        while p1 != p2:
            p = int((p1 + p2)/2)
            if target > nums[p]:
                p1 = p + 1
            elif target < nums[p]:
                p2 = p
            else:
                return p
            if p1 == p2:
                if nums[p1] == target:
                    return p1
                else:
                    break
        return -1
            
#nums = [-1,0,3,5,9,12];target = 9
#nums = [-1,0,3,5,9,12];target = 2
#nums = [5];target = 5
nums = [2,5];target = 5
print(Solution().search(nums, target))