class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        """
        array = []
        ret = []
        for i in range(len(numbers)):
            if numbers[i] not in array:
                array.append(numbers[i])
            else:
                continue
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    ret.append(i + 1)
                    ret.append(j + 1)
                    return ret
        # for i in range(len(numbers)):
        #     numbers[i] = numbers[i] - target
        # ret = []
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == 0:
        #             ret.append(i + 1)
        #             ret.append(j + 1)
        #             return ret
        # print(numbers)
#numbers = [2,7,11,15];target = 22
numbers = []
readStr = ""
lines = []
with open(r'numbers.txt', 'r') as f:
    lines = f.readlines()
for l in lines:
    readStr += l.rstrip('\n')
readStr = readStr.rstrip(']').lstrip('[')
numbers = readStr.split(',')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# print(readStr)
# print(numbers)
target = 2
print(Solution().twoSum(numbers, target))
