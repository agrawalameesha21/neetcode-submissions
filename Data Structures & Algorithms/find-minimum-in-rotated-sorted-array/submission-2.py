class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # get the point at which array was rotated
        while left <= right:
            mid = (right - left) // 2 + left

            # check if l is greater than mid, if yes this half has the point
            # else the right one has
            if nums[mid] > nums[right]:
                if left == mid: left = left + 1
                else: left = mid
            elif nums[mid] < nums[left]:
                if right == mid: right = right - 1
                else: right = mid

            if nums[left] <= nums[right]:
                break


        return nums[left]

