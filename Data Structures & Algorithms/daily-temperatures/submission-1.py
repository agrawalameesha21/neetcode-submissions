class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0]
        
        bucket = []
        res = [0] * len(temperatures)
        for index, n in enumerate(temperatures):
            last_el = 0
            if len(bucket) > 0: 
                last_el = bucket[len(bucket) - 1]
            while len(bucket) > 0 and n > temperatures[last_el]:
                spot = bucket.pop()
                res[spot] = index - spot
                if len(bucket) > 0: last_el = bucket[len(bucket) - 1]
            bucket.append(index)

        return res