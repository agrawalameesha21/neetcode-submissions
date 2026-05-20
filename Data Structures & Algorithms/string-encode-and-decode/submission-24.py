class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for x in strs:
            encoded_str += str(len(x)) + "-"
            for y in x:
                encoded_str += str(ord(y)) + "-"
        
        return encoded_str[:-1]
    

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        
        codes = s.split("-")
        if len(codes) == 1: return [""]
        current_length = int(codes[0])
        prev_length = 0
        strings = []
        string = ""
        for x in range(1, len(codes)):
            # print(x, codes[x], current_length, prev_length)
            if x > current_length + prev_length: 
                # print("x", x)
                strings.append(string)
                prev_length += current_length + 1 # 1 for length of string
                current_length = int(codes[x])
                string = ""
            else:
                string += chr(int(codes[x]))
        strings.append(string)

        # print(strings)
        return strings

            
            
        
    
