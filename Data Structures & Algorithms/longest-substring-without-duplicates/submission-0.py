class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_len = 0
        char_set = set()
        while r < len(s):
            char = s[r]
            if char in char_set:
                char_set.remove(s[l])
                l = l + 1
            else:
                char_set.add(char)
                max_len = max(len(char_set), max_len)
                r = r + 1

        return max_len