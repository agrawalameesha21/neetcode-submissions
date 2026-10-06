class Solution:
    # first check s1 len str and compare each char, get a map and mark the ones present true, if all return true
    # start iteration and check the window if new substr has remaining chars, if not remove the l from map and increase r
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_char_map = {}
        for char in s1:
            if char in s1_char_map:
                s1_char_map[char] = s1_char_map[char] + 1
            else:
                s1_char_map[char] = 1

        l,r = 0, 0
        window_char_map = {}
        while r < len(s2):
            if r - l + 1 > len(s1):
                window_char_map[s2[l]] = window_char_map[s2[l]] - 1
                if window_char_map[s2[l]] == 0: del window_char_map[s2[l]]
                l = l + 1

            char = s2[r]
            if char in window_char_map:
                window_char_map[char] = window_char_map[char] + 1
            else:
                window_char_map[char] = 1
            
            if s1_char_map == window_char_map: return True
            r = r + 1
        
        return False
