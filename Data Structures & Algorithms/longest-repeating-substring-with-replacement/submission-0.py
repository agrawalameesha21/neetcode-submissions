class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        char_map = {}
        max_occuring = 0
        max_len = 0

        while r < len(s):
            char = s[r]
            if char in char_map:
                char_map[char] = char_map[char] + 1
            else:
                char_map[char] = 1
            
            max_occuring = max(max_occuring, char_map[char])

            while r - l + 1 - max_occuring > k:
                char_map[s[l]] = char_map[s[l]] - 1
                l = l + 1

            max_len = max(r - l + 1, max_len)
            r = r + 1

        return max_len

