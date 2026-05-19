class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            if map.get(nums[i]) == None:
                map[nums[i]] = 1;
            else:
                map[nums[i]] += 1;
    
        keys = list(map.keys())
        frequencyBucket = {}
        max_value = 0
        for i in range(len(keys)):
            val = map[keys[i]]
            if val > max_value: max_value = val
            if frequencyBucket.get(val) == None:
                frequencyBucket[val] = [keys[i]]
            else:
                frequencyBucket[val].append(keys[i])

        print(frequencyBucket)
        result = []
        freqKeys = list(frequencyBucket.keys())
        i = max_value
        while i >= 0 and len(result) < k:
            print(i)
            values = frequencyBucket.get(i)
            print(values, i)
            if values != None:
                result.extend(values)
            i -= 1
    
        return result
            

