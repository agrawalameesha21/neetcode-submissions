class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # findRate {
        #     get min rate = ceil(sum/h)
        #     get max(piles) = get the max value in all piles
        #     for min to max, use binary search and keep applying canFinish(k) to the mid
        #     if true, go left else go right
        #     if only one value remains, return the answer
        # }

        sum = 0
        maxPile = 0
        for pile in piles:
            sum = sum + pile
            maxPile = max(maxPile, pile)

        left = (sum + h - 1)//h
        right = maxPile
        while left < right:
            mid = (right + left) // 2

            if self.canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left


    def canFinish(self, piles: List[int], h: int, k: int) -> int:
        # canFinish(k) {
        # iterate through piles
        # get the hrs with k
        # if hrs <= h, return true else false
        # }

        total_h = 0
        for pile in piles:
            total_h = total_h + (pile + k - 1)//k
            if total_h > h: return False

        return total_h <= h

