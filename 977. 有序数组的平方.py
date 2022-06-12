class Solution(object):
    def QuickSort(self, array, i, j):
        if (j - i) < 1:
            return array
        pivot = array[i]
        left = i
        right = j
        flag = 1
        while left < right:
            if flag == 1:
                if array[right] < pivot:
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
        array[left] = pivot
        array = self.QuickSort(array, i ,left - 1)
        array = self.QuickSort(array, left + 1, j)
        return array
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        self.QuickSort(nums, 0, len(nums) - 1)
        return nums
nums = [-4,-1,0,3,10]
print(Solution().sortedSquares(nums))
