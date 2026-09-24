class Solution:
    def search(self, nums: List[int], target: int) -> int:
       return self.divideAndFind(nums, target, 0)

    def divideAndFind(self, nums: List[int], target: int, start_index: int) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1:
            if nums[0] == target:
                return start_index
            else: return -1
        
        half = len(nums)//2
        print(half, nums, start_index)
        index = -1
        if nums[half] <= target:
            index = self.divideAndFind(nums[half: ], target, start_index + half)
        else:
            index = self.divideAndFind(nums[0:half], target, start_index)
        return index
