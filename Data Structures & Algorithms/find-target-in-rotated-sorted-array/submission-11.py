class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # get the point at which array was rotated
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target: return mid

            # check if l is greater than mid, if yes this half has the point
            # else the right one has
            if nums[mid] >= nums[right]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1