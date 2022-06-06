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
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == len(nums1):
            return nums1
        if m < len(nums1):
            for i in range(n):
                nums1[m + i] = nums2[i]
        nums1 = self.QuickSort(nums1,0,len(nums1) - 1)
nums1 = [1,2,3,0,0,0];m = 3;nums2 = [2,5,6];n = 3
#nums1 = [1];m = 1;nums2 = [];n = 0
#nums1 = [0];m = 0;nums2 = [1];n = 1
Solution().merge(nums1, m, nums2, n)
print(nums1)
