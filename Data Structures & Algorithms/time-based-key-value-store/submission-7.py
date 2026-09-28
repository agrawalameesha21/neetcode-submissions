class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # search the map for key. if not push the key and [value, ts]
        if key not in self.timeMap:
            self.timeMap[key] = []

        # if yes, search for key and push [value, ts]
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # get the values for key, if empty return ""
        if key not in self.timeMap:
            return ""
        
        # if values present, do binary search for max or equal timestamp
        # set is increasing so array is already sorted
        values = self.timeMap[key]

        if len(values) == 1:
            if values[0][1] <= timestamp:
                return values[0][0]
            else: return ""

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (right - left + 1) // 2 + left 
            if values[mid][1] < timestamp:
                if mid == left: left = left + 1
                else: left = mid
            elif values[mid][1] > timestamp:
                if mid == right: right = right - 1
                else: right = mid
            else:
                return values[mid][0]

            if right == left and values[right][1] <= timestamp:
                return values[right][0]

        return ""
        
