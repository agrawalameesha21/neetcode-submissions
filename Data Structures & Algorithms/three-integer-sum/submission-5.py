class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2: return []
        sortedArr = sorted(nums)

        result = []
        for i, targetIndex in enumerate(sortedArr):
            firstIndex = i + 1
            secondIndex = len(sortedArr) - 1

            if i > 0 and sortedArr[i] == sortedArr[i-1]: continue

            while firstIndex < secondIndex:
                sum = sortedArr[firstIndex] + sortedArr[secondIndex] + sortedArr[i]
                # print(firstIndex, secondIndex, i)
                if sum == 0:
                    result.append([sortedArr[i], sortedArr[firstIndex], sortedArr[secondIndex]])
                    firstIndex = firstIndex + 1 
                    secondIndex = secondIndex - 1 
                    while firstIndex < secondIndex and sortedArr[firstIndex] == sortedArr[firstIndex - 1]:
                        firstIndex = firstIndex + 1 
                elif sum < 0:
                    firstIndex = firstIndex + 1 
                else:
                    secondIndex = secondIndex - 1 
                    
        return result
    