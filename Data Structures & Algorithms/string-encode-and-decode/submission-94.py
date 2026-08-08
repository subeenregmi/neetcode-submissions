class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            if string == "":
                encoded += "-1,"
            else:
                for char in string:
                    encoded += str(ord(char))
                    encoded += ","
            
            encoded = encoded[:-1]
            encoded += "!"

        return encoded[:-1]

    def decode(self, s: str) -> List[str]:
        words = []
        print(s)
        if s == "":
            return []

        for enc_word in s.split("!"):
            word = ""
            for enc_char in enc_word.split(","):
                ascii_char = int(enc_char)
                if ascii_char == -1:
                    word = ""
                else:
                    word += chr(ascii_char)

            words.append(word)

        return words

