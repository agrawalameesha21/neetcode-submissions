class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        i = 0
        j = len(heights) - 1
        while i < j:
            minHeight = 0
            if heights[i] > heights[j]: minHeight = heights[j] 
            else: minHeight = heights[i]

            vol = minHeight * (j - i)
            if vol > maxVol: maxVol = vol
            if heights[i] > heights[j]: 
                j = j - 1
            else:
                i = i + 1

        return maxVol

