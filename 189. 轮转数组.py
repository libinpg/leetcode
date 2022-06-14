class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #print(nums)
        ret = []
        for n in nums:
            ret.append(n)
        for i in range(len(nums)):
            #print(nums[i])
            nums[(i+k) % len(ret)] = ret[i]
            #print(i,(i+1) % len(ret),nums[i])
        #print(ret)
        return nums 
nums = [1,2,3,4,5,6,7];k = 3
print(Solution().rotate(nums, k))