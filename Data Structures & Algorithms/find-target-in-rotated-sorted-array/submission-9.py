class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        # now break the arrays in two from the points its rotated and get the half which can have target
        #  apply bs for that half again
        if left == 0: return self.b_search(nums, target, 0)

        array_1 = nums[0:left]
        array_2 = nums[left:]
        if array_1[0] <= target and array_1[len(array_1) - 1] >= target: return self.b_search(array_1, target, 0)
        else: return self.b_search(array_2, target, left)

    def b_search(self, nums: List[int], target: int, start_index: int) -> int:
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (right - left) // 2 + left

            # check if mid is greater than target, if yes update left as mid
            # else the right as mid
            if nums[mid] < target:
                if left == mid: left = left + 1
                else: left = mid
            elif nums[mid] > target:
                if right == mid: right = right - 1
                else: right = mid
            elif nums[mid] == target:
                return mid + start_index

        return -1