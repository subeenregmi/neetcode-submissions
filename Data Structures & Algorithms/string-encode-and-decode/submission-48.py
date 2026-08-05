class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for x in strs:
            enc += (f"{str(len(x))} {x} ")
        return enc[:-1]
        print(enc)

    def decode(self, s: str) -> List[str]:
        d = []
        i = 0
        num = ""
        lengthGet = True
        length = 0
        print(s)
        while i < len(s) or not lengthGet:
            if lengthGet:
                if s[i] == " ":
                    i+=1
                    lengthGet = False
                    length = int(num)
                else:
                    num += s[i]
                    i += 1
            else:
                if length == 0:
                    d.append("")
                else:
                    d.append(s[i:i+length])
                i += length + 1
                num = ""
                lengthGet = True

        
        return d


            
