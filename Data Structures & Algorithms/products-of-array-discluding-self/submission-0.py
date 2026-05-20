class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zero = False
        has_two_zeroes = False
        product = 1
        result = []

        for x in nums:
            if x == 0: 
                if has_zero == False:
                    has_zero = True
                else:
                    has_two_zeroes = True
                    break
            else:
                product *= x

        if has_two_zeroes:
            for x in nums:
                result.append(0)
            return result

        for x in nums:
            if has_zero and x != 0:
                result.append(0)
            elif has_zero and x == 0:
                result.append(product)
            else:
                result.append(int(product/x))

        return result