class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        # shortest substr of t
        # include duplicates
        # not need to be consecutive
        # variable window

        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] = t_map[char] + 1
            else:
                t_map[char] = 1
        
        s_map = {}
        l, r = 0, 0
        satisfied = 0
        output = ""
        while r < len(s):
            char = s[r]
            if char in t_map:
                if char in s_map:
                    s_map[char] = s_map[char] + 1
                else:
                    s_map[char] = 1
                if s_map[char] == t_map[char]: satisfied = satisfied + 1
            
            while satisfied >= len(t_map):
                char = s[l]
                if satisfied == len(t_map): 
                    if len(output) > r - l + 1 or len(output) == 0:
                        output = s[l:r+1]
                if char in s_map:
                    s_map[char] = s_map[char] - 1
                    if s_map[char] < t_map[char]: satisfied = satisfied - 1
                l = l + 1
                
            r = r + 1

        return output

