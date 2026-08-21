class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0: return [0,0]

        start = 0
        end = len(numbers) - 1
        while start < end:
            current_sum = numbers[start] + numbers[end]
            if current_sum == target:
                return [start + 1, end + 1]
            elif current_sum > target:
                end = end - 1
            else:
                start = start + 1