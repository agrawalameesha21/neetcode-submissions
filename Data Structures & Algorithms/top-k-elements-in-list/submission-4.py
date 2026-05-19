class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if map.get(nums[i]) == None:
                map[nums[i]] = 1;
            else:
                map[nums[i]] += 1;
    
        keys = list(map.keys())
        frequency_bucket = {}
        max_value = 0
        for i in range(len(keys)):
            val = map[keys[i]]
            if val > max_value: max_value = val
            if frequency_bucket.get(val) == None:
                frequency_bucket[val] = [keys[i]]
            else:
                frequency_bucket[val].append(keys[i])

        result = []
        i = max_value
        while i >= 0 and len(result) < k:
            values = frequency_bucket.get(i)
            if values != None:
                result.extend(values)
            i -= 1
    
        return result
            

