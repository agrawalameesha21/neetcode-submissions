class Solution:
    def isPalindrome(self, s: str) -> bool:
        strArr = []
        for letter in s:
            if letter.isalnum():
                strArr.append(letter.lower())

        if len(strArr) == 0: return True

        start = 0
        end = len(strArr) - 1
        while start <= end:
            print(start, end)
            if strArr[start] != strArr[end]:
                return False
            start = start + 1 
            end = end - 1

        return True