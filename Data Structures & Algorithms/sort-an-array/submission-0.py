class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, nums):
        if len(nums) <= 1: return nums
        
        mid = int(len(nums)/2)
        arr1 = self.merge_sort(nums[:mid])
        arr2 = self.merge_sort(nums[mid:])
        return self.sort(arr1, arr2)

    def sort(self, arr1, arr2):
        arr2_pointer = 0;
        merged_array = []
        for i in range(len(arr1)):
            for j in range(arr2_pointer, len(arr2)):
                if arr1[i] > arr2[j]:
                    merged_array.append(arr2[j])
                    arr2_pointer += 1
                else:
                    break
            merged_array.append(arr1[i])

        if arr2_pointer != len(arr2): merged_array.extend(arr2[arr2_pointer:])
        return merged_array
        