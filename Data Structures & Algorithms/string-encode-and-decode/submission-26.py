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
        strings = []
        string = ""
        for x in range(1, len(codes)):
            if x > current_length: 
                strings.append(string)
                current_length += int(codes[x]) + 1 # 1 for length of string
                string = ""
            else:
                string += chr(int(codes[x]))
        strings.append(string)
        return strings

            
            
        
    
