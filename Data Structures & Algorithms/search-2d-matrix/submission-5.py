class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if m[len(m) - 1] >= target:
                return self.search(m, target)
    
        return False

    def search(self, arr: List[int], target: int) -> bool:
        if len(arr) == 1:
            return arr[0] == target

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            if arr[mid] < target:
                if left == mid: left = left + 1
                else: left = mid
            elif arr[mid] > target:
                if right == mid: right = right - 1
                else: right = mid
            elif arr[mid] == target:
                return True

        return False
